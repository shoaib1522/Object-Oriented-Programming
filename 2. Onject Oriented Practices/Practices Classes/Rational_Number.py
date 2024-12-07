class rational:
    def __new__(cls,Numerator=0,Denominator=1):
        print(f'Creating Fraction ({Numerator},{Denominator})')
        obj=super().__new__(cls)
        return obj
    def __init__(self,Numerator=0,Denominator=1):
        self.__Numerator=Numerator
        self.__Denominator=Denominator
        return
    @property
    def Numerator(self):
        return self.__Numerator
    @Numerator.setter
    def Numerator(self,n):
        self.__Numerator=n
        return
    @property
    def Denominator(self):
        return self.__Denominator    
    @Denominator.setter
    def Denominator(self,d):
        if d!=0:
            self.__Denominator=d
        else:
            self.__Denominator=1
        return
    def __str__(self):
        return f"Fraction is: {self.__Numerator}\n\t     --\n\t     {self.__Denominator}"
    def __add__(self,Sec_Fraction):
        Add_Fraction=rational()
        Add_Fraction.Numerator=(self.__Numerator*Sec_Fraction.__Denominator)+(self.__Denominator*Sec_Fraction.__Numerator)
        Add_Fraction.Denominator=self.__Denominator*Sec_Fraction.Denominator
        return Add_Fraction
    def __sub__(self,Sec_Fraction):
        Sub_Fraction=rational()
        Sub_Fraction.Numerator=(self.__Numerator*Sec_Fraction.__Denominator)-(self.__Denominator*Sec_Fraction.__Numerator)
        Sub_Fraction.Denominator=self.__Denominator*Sec_Fraction.Denominator
        return Sub_Fraction
    def __mul__(self,Sec_Fraction):
        mul_Fraction=rational()
        mul_Fraction.Numerator=(self.__Numerator*Sec_Fraction.__Numerator)
        mul_Fraction.Denominator=self.__Denominator*Sec_Fraction.Denominator
        return mul_Fraction
    def __truediv__(self,Sec_Fraction):
        Div_Fraction=rational()
        Div_Fraction.Numerator=self.__Numerator*Sec_Fraction.Denominator
        Div_Fraction.Denominator=self.__Denominator*Sec_Fraction.Numerator
        return Div_Fraction
    def real_number(self):
        real=self.Numerator/self.Denominator
        return real
def main(): 
    first_fraction=rational(10,250)
    print(first_fraction)
    Second_fraction=rational(15,26)
    print(Second_fraction)
    print('Addition is:')
    print(str(first_fraction+Second_fraction))
    print('Subtraction is:')
    print(str(first_fraction-Second_fraction))
    print('Multiplication  is:')
    print(str(first_fraction*Second_fraction))
    print('Division is:')
    print(str(first_fraction/Second_fraction))
    real=rational.real_number(first_fraction)
    print('The real fraction is:',real)
if __name__ == "__main__":
    main()