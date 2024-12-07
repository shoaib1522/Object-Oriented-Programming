class Canvas(object):
    # __shapes={"Triangle","Rectangle","Circle","Square","Oval"}
    def __init__(self,name,outline,Background):
        self.__name=name
        self.__outline=outline
        self.__background=Background
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,Nm):
        self.__name=Nm
        return self.__name
    @property
    def background(self):
        return self.__background
    @background.setter
    def name(self,Bg):
        self.__background=Bg
        return self.__background
    def __str__(self):
        return " Name: {} , Background: {} ".format(self.__name,self.__background) + f'{self.__outline}'
