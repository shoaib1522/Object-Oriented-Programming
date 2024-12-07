from Canvas import Canvas
class Shape(Canvas):
    def __init__(self,name,outline,outline_color,Background,Type,Location):
        super().__init__(name, outline, Background)
        self.__location=Location
        self.__type=Type
        self.__color=outline_color
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self,loc):
        self.__location=loc
        return self.__location
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,ty):
        self.__type=ty
        return self.__type
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,col):
        self.__color=col
        return self.__color
    def __str__(self):
        return " Type: {} , Outline Color: {} \n".format(self.__type,self.__color) + super().__str__() + f'{self.__location}'
    