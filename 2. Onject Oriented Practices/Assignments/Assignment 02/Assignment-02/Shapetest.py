from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Oval import Oval
from Outline import Outline
from Point import Point
def main():
    # SHAPE 1:
    print('Shape 1: ')
    Sq_1_outline=Outline(True) 
    Sq_1_point=Point("Center")
    Sq_1=Square("Shape 1",Sq_1_outline,"Red","White",'Square',Sq_1_point,5)
    print(Sq_1)
    print('Area Of Shape 1 is:',Sq_1.area())
    print('Perimeter Of Shape 1 is:',Sq_1.perimeter())
    print('Length Of Diagonal Of Shape 1 is:',Sq_1.length_of_diagonal_square())
    # SHAPE 2:
    print('Shape 2: ')
    Rc_1_outline=Outline(True) 
    Rc_1_point=Point("Bottom")
    Rc_1=Rectangle("Shape 2",Rc_1_outline,"Blue","Caramel",'Rectangle',Rc_1_point,6,2)
    print(Rc_1) 
    print('Area Of Shape 2 is:',Rc_1.area())   
    print('Perimeter Of Shape 2 is:',Rc_1.perimeter())   
    print('Length Of Diagonal Of Shape 2 is:',Rc_1.length_of_diagonal_rectangle())   
    # SHAPE 3:
    print('Shape 3: ')
    Cir_1_outline=Outline(False) 
    Cir_1_point=Point("Upper-Of-Canvas")
    Cir_1=Circle("Shape 3",Cir_1_outline,"Sky-Blue","Tan",'Circle',Cir_1_point,25)
    print(Cir_1)
    print('Area Of Shape 3 is:',Cir_1.area()) 
    print('Circumference Of Shape 3 is:',Cir_1.circumference()) 
    print('Diameter Of Shape 3 is:',Cir_1.diameter()) 
    # SHAPE 4:
    print('Shape 4: ')
    Ov_1_outline=Outline(True) 
    Ov_1_point=Point("Lower-Right")
    Ov_1=Oval("Shape 4",Ov_1_outline,"Pink","White",'Oval',Ov_1_point,25,28)
    print(Ov_1)
    print('Area Of Shape 4 is:',Ov_1.area())  
    print('Perimeter Of Shape 4 is:',Ov_1.perimeter())  
    # SHAPE 5:
    print('Shape 5: ')
    Tr_1_outline=Outline(True) 
    Tr_1_point=Point("Bottom-Left")
    Tr_1=Triangle("Shape 4",Tr_1_outline,"Green","Painty",'Triangle',Tr_1_point,6,8,11,12,15)
    print(Tr_1)
    print('Area Of Shape 5 is:',Tr_1.area())  
    print('Perimeter Of Shape 5 is:',Tr_1.perimeter())  
main()