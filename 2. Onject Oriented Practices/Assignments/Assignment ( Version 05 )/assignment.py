import struct
def add_data(w1,w2,w3):
    file=open(w1,'r')
    f1=open(w2,'wb')
    f2=open(w3,'wb')
    lst=file.readlines()
    file.close()
    for line in lst:
        x=line.strip().split()
        x[4]=x[4].replace("_"," ")
        n=x[0]
        n=n[1:3].strip()
        b=x[1]+" "+x[2]
        c=float(x[-2])
        d=x[-1]
        fmt='10s40s2sif11s'
        br=struct.pack(fmt,x[0].encode(),b.encode(),n.encode(),int(x[3]),c,d.encode())
        br2=struct.pack('40s10sf',x[4].encode(),x[0].encode(),c)
        f1.write(br2)
        f2.write(br)
    f2.close()
    f1.close()

def add_students(file,skip=0):
    w=input("Enter rollno: ")
    if (check_if_student_data_exists(file,w))==False:
        d=w[1:3]
        x=input("Enter name: ")
        y=float(input("Enter last semester percentage marks: "))
        z=input("Enter phone number: ")
        fmt='10s40s2sf11s'
        f2=open(file,"ab")   
        struct_len = struct.calcsize(fmt)
        f2.seek(skip*struct_len)
        br=struct.pack(fmt,w.encode(),x.encode(),d.encode(),y,z.encode())
        f2.write(br)
        f2.close()
        return "Record added successfully"
    return "Data already exists in file "

def check_if_student_data_exists(file,rollno):
    struct_fmt='10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    with open(file, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            ro=s[0].decode()
            ro=ro.strip()
            if rollno==ro:
                return True
    return False
def grades(grade):
        if grade>=85 and grade<=100:
            return "A"
        elif grade>=80:
            return "A-"
        elif grade>=75:
            return "B+"
        elif grade>=70:
            return "B"
        elif grade>=65:
            return "B-"
        elif grade>=61:
            return "C+"
        elif grade>=58:
            return "C"
        elif grade>=55:
            return "C-"
        elif grade>=50:
            return "D"
        else:
            return "F"
        
def view_grades_of_student(file,name):
    struct_fmt='10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    naam=struct.pack('40s',name.encode())
    x=1
    with open(file, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            if s[1]==naam:
                f2=open('gradesdata.txt','rb')
                length=struct.calcsize('40s10sf')
                f2.seek((x-1)*length)
                z=f2.read(length)
                z2=struct.unpack('40s10sf',z)
                f2.close()
                print(z2[0].decode(), grades(s[4]))
            x+=1
 
def view_grades_of_student_by_rollno(file,rollno):
    struct_fmt='10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    x=1
    with open(file, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            if s[0].decode()==rollno:
                f2=open('gradesdata.txt','rb')
                length=struct.calcsize('40s10sf')
                f2.seek((x-1)*length)
                z=f2.read(length)
                z2=struct.unpack('40s10sf',z)
                f2.close()
                print(z2[0].decode(), grades(s[4]))
            x+=1
 
    
def check_if_student_record_exists(file,line):
    struct_fmt='10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    with open(file, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            if data==line:
                return True
    return False
def view_student_by_rollno(file,rollno):
    struct_fmt='10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    with open(file, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            ro=s[0].decode()
            ro=ro.strip()
            if rollno==ro:
                w=s[1].decode()
                print(s[0].decode(),end=' ')
                print(w.ljust(70),end=' ')
                print(s[2].decode(),end=" ")
                print(s[3],end=' ')
                print(f'{s[4]:.2f}',end=' ')
                print(s[5].decode())


def edit_student_by_rollno(file,rollno):
    d=rollno[1:3]
    x=input("Enter name: ")
    y=float(input("Enter last semester percentage marks: "))
    z=input("Enter phone number: ")
    s=int(input("Enter semester number: "))
    fmt='10s40s2sif11s'
    struct_len = struct.calcsize(fmt)
    struct_fmt = '10s40s2sif11s'
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    br=struct.pack(fmt,rollno.encode(),x.encode(),d.encode(),s,y,z.encode())
    if (check_if_student_record_exists(file,br))==True:
        return "Data already exists in file "
    with open(file, "rb") as f:
        skip=1
        r=1
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            ro=s[0].decode()
            ro=ro.strip()
            if rollno==ro:
                r=skip
            skip+=1
    f2=open(file,'rb+')        
    f2.seek((r-1)*struct_len)
    f2.write(br)
    f2.close()
    return "Record added successfully"
            

def delete_student_by_rollno(file,rollno):
    struct_fmt = '10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from
    with open(file, "rb") as f:
        x=1
        r=1
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            if rollno==s[0].decode:
                r=x
                break
            x+=1
    f=open(file,'rb+')
    f.seek((r-1)*struct_len)
    f.write(struct.pack("71s",("-"*71).encode()))
    f.close()
    return 'Record deleted successfully'

def list_student_by_semester(file,sem):
    struct_fmt='10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    with open(file, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            ro=s[3]
            if ro==sem:
                w=s[1].decode()
                print(s[0].decode(),end=' ')
                print(w.ljust(70),end=' ')
                print(s[2].decode(),end=" ")
                print(s[3],end=' ')
                print(f'{s[4]:.2f}',end=' ')
                print(s[5].decode())

def list_student_by_name(file):
    struct_fmt = '10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from
    with open(file, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            w=s[1].decode()
            print(w)
            print(s[0].decode(),end=' ')
            print(s[2].decode(),end=" ")
            print(s[3],end=' ')
            print(f'{s[4]:.2f}',end=' ')
            print(s[5].decode())
            print()

def student_list(file):
    struct_fmt = '10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from
    with open(file, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            w=s[1].decode()
            print(s[0].decode(),end=' ')
            print(w.ljust(70),end=' ')
            print(s[2].decode(),end=" ")
            print(s[3],end=' ')
            print(f'{s[4]:.2f}',end=' ')
            print(s[5].decode())
def list_coursewise_grades_of_student(file,file2,course):
    struct_fmt='40s10sf'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    print('Course Title: ',course.decode())
    with open(file, "rb") as f:
        x=1
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            if course==s[0]:
                f2=open(file2,'rb')
                fmt = '10s40s2sif11s'
                len = struct.calcsize(fmt)
                structunpack = struct.Struct(fmt).unpack_from
                f2.read((x-1)*len)
                r=f2.read(len)
                e=structunpack(r)
                print(e[1].decode(),grades(e[4]))
                f2.close()
                
            x+=1    
            
def edit_grademarks_by_name(file,rollno):
    d=rollno[1:3]
    x=input("Enter name: ")
    y=float(input("Enter last semester percentage marks: "))
    z=input("Enter phone number: ")
    s=int(input("Enter semester number: "))
    fmt='10s40s2sif11s'
    struct_len = struct.calcsize(fmt)
    struct_fmt = '10s40s2sif11s'
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    br=struct.pack(fmt,rollno.encode(),x.encode(),d.encode(),s,y,z.encode())
    if (check_if_student_record_exists(file,br))==True:
        return "Correct Data already exists "
    with open(file, "rb") as f:
        skip=1
        r=1
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            ro=s[0].decode()
            ro=ro.strip()
            if rollno==ro:
                r=skip
            skip+=1
    f2=open(file,'rb+')        
    f2.seek((r-1)*struct_len)
    w='10s40s2si'
    w=struct.calcsize(w)
    f.seek(w)
    f2.write(struct.pack('f',y))
    f2.close()
    return "Grade edited successfully"
 
 
def add_grademarks_by_name(file,rollno):
    d=rollno[1:3]
    x=input("Enter name: ")
    y=float(input("Enter last semester percentage marks: "))
    z=input("Enter phone number: ")
    s=int(input("Enter semester number: "))
    fmt='10s40s2sif11s'
    struct_len = struct.calcsize(fmt)
    struct_fmt = '10s40s2sif11s'
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    br=struct.pack(fmt,rollno.encode(),x.encode(),d.encode(),s,y,z.encode())
    if (check_if_student_record_exists(file,br))==True:
        return "Correct Data already exists "
    with open(file, "rb") as f:
        skip=1
        r=1
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            ro=s[0].decode()
            ro=ro.strip()
            if rollno==ro:
                r=skip
            skip+=1
    f2=open(file,'ab')        
    f2.write(struct.pack('10s40s2sif11s',y))
    f2.close()
    return "Grade edited successfully"           

def delete_grade_marks_by_name(file,rollno):
    struct_fmt = '10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from
    with open(file, "rb") as f:
        x=1
        r=1
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            if rollno==s[0].decode:
                r=x
                break
            x+=1
    f=open(file,'rb+')
    f.seek((r-1)*struct_len)
    w='10s40s2si'
    w=struct.calcsize(w)
    f.seek(w)
    f.write(struct.pack("s",'~'.encode()))
    f.close()
    return 'Grade deleted successfully' 
          
def award_sheet():
    courses=['Introduction to Computing','Programming Fundamentals','Introduction to Data Science','Programming Fundamentals','Object Oriented Programming']
    for course in courses:
        r=struct.pack('40s',course.encode())
        list_coursewise_grades_of_student('gradesdata.txt','studentsdata.txt',r)
        print()
def list_coursewise_data_of_student(file,file2,course):
    struct_fmt='40s10sf'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from   
    print('Course Title: ',course.decode())
    with open(file, "rb") as f:
        x=1
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            if course==s[0]:
                f2=open(file2,'rb')
                fmt = '10s40s2sif11s'
                len = struct.calcsize(fmt)
                structunpack = struct.Struct(fmt).unpack_from
                f2.read((x-1)*len)
                r=f2.read(len)
                e=structunpack(r)
                t=e[1].decode()
                print(f'{e[0].decode()} {t.ljust(30)}{e[4]:.2f}  {grades(e[4])}')
                f2.close()
                
            x+=1        
def summary_sheet():
    courses=['Introduction to Computing','Programming Fundamentals','Introduction to Data Science','Programming Fundamentals','Object Oriented Programming']
    for course in courses:
        r=struct.pack('40s',course.encode())
        list_coursewise_data_of_student('gradesdata.txt','studentsdata.txt',r)
        print()
          
def Transcript(file,x):
    struct_fmt = '10s40s2sif11s'
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from
    d=0
    with open(file, "rb") as f:
        while True and d<x:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            w=s[1].decode()
            print(s[0].decode(),end=' ')
            print(w.ljust(40),end=' ')
            print(s[2].decode(),end=" ")
            print(s[3],end=' ')
            print(f'{s[4]:.2f}',end=' ')
            print(s[5].decode())
            d+=1
        
def main():
    print("Enter options from the following menu:")
    print("1. QUIT\n2. Add a student\n3. View a student by roll no\n4. Edit student by roll no\n5. Delete student by roll no\n6. List student by semester \n7. List student by name\n8. Print students list\n9. Add grade of a student for a course\n10. Import grades for a course for many students from a TABed text file\n11. View grades of a student\n12. List Student wise (1 student) grade of courses\n13. List Course wise grade of students\n14. Award sheet (courses one by one, with students enrolled in it)\n15. Summary sheet (courses info, one by one, with one line for each student in it)\n16. Transcripts")
    x=int(input('input: '))
    while x>18 or x<1:
        print("Enter options from the following menu:")
        print("1. QUIT\n2. Add a student\n3.View a student by roll no\n4.Edit student by roll no \n5.Delete student by roll no\n6.List student by semester\n7.List student by name\n8.Print students list\n9.Add grade of a student for a course\n10. Import grades for a course for many students from a TABed text file (NO DUPS)\n11. View grades of a student\n12. List Student wise (1 student) grade of courses\n13. List Course wise grade (1 course) of students\n14. Award sheet \n15. Summary sheet\n16. Transcripts")
        x=int(input('input: '))
    if x==1:
        print("Course Management system exited")
    elif x==2:
        print(add_students('studentsdata.txt'))
    elif x==3:
        rollno=input('Enter roll no of student record you want to view: ')
        view_student_by_rollno('studentsdata.txt',rollno)
    elif x==4:
        rollno=input('Enter roll no of student record you want to edit: ')
        print(edit_student_by_rollno('studentsdata.txt',rollno))
    elif x==5:
        rollno=input('Enter roll no of student record you want to delete: ')
        print(delete_student_by_rollno('studentsdata.txt',rollno))
    elif x==6:
        sem=int(input('Enter semester number of students record you want to view: '))
        list_student_by_semester('studentsdata.txt',sem)
    elif x==7:
        list_student_by_name('studentsdata.txt')
    elif x==8:
        student_list('studentsdata.txt')
    elif x==9:
        rollno=input('Enter roll no of student record you want to add: ')
        add_grademarks_by_name('studentsdata.txt',rollno)
    elif x==10:
        f1='data2.txt'
        f2='gradesdata.txt'
        f3='studentsdata.txt'
        add_data(f1,f2,f3)
    elif x==11:
        name=input('Enter name of student: ')
        view_grades_of_student('studentsdata.txt',name)
    elif x==12:
        student_list('studentsdata.txt')
    elif x==13:
        course=input("enter course name: ")
        course=struct.pack('40s',course.encode())
        list_coursewise_grades_of_student('gradesdata.txt','studentsdata.txt',course)
    elif x==14:
        award_sheet()
    elif x==15:
        summary_sheet()
    elif x==16:
        x=int(input('Enter the number of students transcipt you want view: '))
        Transcript('studentsdata.txt',x)
           
        
    
main()