# Introduction of user defined type, here named Vector, a class
# Introduction to properties, and __new__/__del__ member functions
# __main__ and __name__

class Vector:
    def __new__(cls, x=0, y=0, z=0):
        print(f"creating a Vector ({x},{y},{z})")    
        obj = super().__new__(cls)
        return obj
    def __del__(self):
        print(f"{self} is getting garbage")
        return
    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z
        return
    @property
    def X(self):
        return self.__x
    @X.setter
    def X(self, d):
        self.__x = d
        return
    @property
    def Y(self):
        return self.__y
    @Y.setter
    def Y(self, d):
        self.__y = d
        return
    @property
    def Z(self):
        return self.__z
    @Z.setter
    def Z(self, d):
        self.__z = d
        return

    def __str__(self):
        return "(" + str(self.X) + "," + str(self.Y) + "," + str(self.Z) + ")"
    def __add__(lhs, rhs):
        v = Vector()
        v.X = lhs.X + rhs.X
        v.Y = lhs.Y + rhs.Y
        v.Z = lhs.Z + rhs.Z
        return v
    @staticmethod
    def stp(v1, v2, v3):
        v = v1.X * (v2.Y * v3.Z - v2.Z * v3.Y)
        v -= v1.Y * (v2.X * v3.Z - v2.Z * v3.X)
        v += v1.Z * (v2.X * v3.Y - v2.Y * v3.X)
        return v

def main():
    t = Vector(2,1,5)
    m = Vector(3,-2,4)
    b = Vector(4,-1,-2)
    print("t: " + str(t))
    print("m: " + str(m))
    print("b: " + str(b))
    print("t+b: " + str(t+b))
    print("stp: " + str(Vector.stp(t,m,b)))

if __name__ == "__main__":
    main()
    
