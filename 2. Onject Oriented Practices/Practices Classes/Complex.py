class ComplexNumbers:
    def __new__(cls,real=0,imaginary=0):
        # print(f'Creating a Complex Number: ({real},{imaginary})')
        obj=super().__new__(cls)
        return obj
    def __init__(self,real=0,imaginary=0):
        self.real=real
        self.imaginary=imaginary
        return
    def __str__(self) :
        if self.imaginary<0:
            return '{}{}i'.format(self.real,(self.imaginary))
        return '{}+{}i'.format(self.real,(self.imaginary))
    def __add__(self,sec_complex):
        Add_Comp=ComplexNumbers()
        Add_Comp.real=self.real+sec_complex.real
        Add_Comp.imaginary=self.imaginary+sec_complex.imaginary
        return Add_Comp
    
    def __sub__(self,sec_complex):
        Sub_Comp=ComplexNumbers()
        Sub_Comp.real=self.real-sec_complex.real
        Sub_Comp.imaginary=self.imaginary-sec_complex.imaginary
        return Sub_Comp
    
    def __mul__(self,sec_complex):
        Mul_Comp=ComplexNumbers()
        Mul_Comp.real=(self.real*sec_complex.real)+(self.imaginary*sec_complex.imaginary*-1)
        Mul_Comp.imaginary=(self.imaginary*sec_complex.real)+(self.real*sec_complex.imaginary)
        return Mul_Comp
    def conjugate(self):
        conjugate=ComplexNumbers()
        conjugate.real=self.real
        conjugate.imaginary= -1 *self.imaginary
        return conjugate
    def __truediv__(self,sec_complex):
        Upper=ComplexNumbers()
        Upper=self*(ComplexNumbers.conjugate(sec_complex))
        Lower=ComplexNumbers()
        Lower=sec_complex*(ComplexNumbers.conjugate(sec_complex))
        Division_Comp=ComplexNumbers()
        Division_Comp.real=Upper.real/Lower.real
        Division_Comp.imaginary=Upper.imaginary/Lower.real
        return Division_Comp
    def mode(self):
        mode=((self.real)**2+(self.imaginary**2))**0.5
        return mode
    

def main():
    first_comp=ComplexNumbers(5,-5)
    print(f'The first CompleX number is :', str(first_comp))
    second_comp=ComplexNumbers(3,6)
    print(f'The Second CompleX number is :', str(second_comp))
    print(f'Addition of them is: ',str(first_comp+second_comp))
    print(f'Subtraction of them is: ',str(first_comp-second_comp))
    print(f'Multiplication of them is: ',str(first_comp*second_comp))
    print(f'Division of them is: ',str(first_comp/second_comp))
    print(f'Mode of first Complex is: ',ComplexNumbers.mode(first_comp))
main()