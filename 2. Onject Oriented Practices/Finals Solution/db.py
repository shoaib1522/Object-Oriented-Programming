import sqlite3
conn = sqlite3.connect('University.db')
cursor = conn.cursor()
# cursor.execute('Create table university (rollno integer primary key,name text,semester integer,gpa real)')
# for i in range(3):
#     roll=int(input('Enter Roll: '))
#     name=(input('Enter name: '))
#     sem=(input('Enter Sem: '))
#     gpa=float(input('Enter GPA: '))
#     cursor.execute(f'Insert Into university Values ({roll},"{name}","{sem}",{gpa})')
# c=cursor.execute('SELECT * FROM university WHERE name="shiza"')
# name=c.fetchone()
# if name:
#     print('Exists')
# else:
#     print('not Exists')
# namee='shiza'
# cursor.execute(f"update university set name='john' where name='{namee}'")
# print(c.fetchmany(2))

cursor.execute('Delete from university where rollno=2')
conn.commit()
cursor.close()
conn.close()