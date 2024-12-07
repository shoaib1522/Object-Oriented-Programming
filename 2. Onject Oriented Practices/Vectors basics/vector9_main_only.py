# from vector9 import Vector
# from vector9 import main as main

import vector9

def main():
    t = Vector(2,1,5)
    m = Vector(3,-2,4)
    b = Vector(4,-1,-2)
    print("t: " + str(t))
    print("m: " + str(m))
    print("b: " + str(b))
    print("t+b: " + str(t+b))
    print("stp: " + str(Vector.stp(t,m,b)))

if __name__ == "__main__":    # if this line is removed in vector9.py, the output is generated twice, as on loading its main is also called
    vector9.main()
    
