import math

class Circulo:

    def __init__(self, radio):
        self.__radio = radio
    def setRadius(self, radio):
        self.__radio = radio
    def getRadio(self):
        return self.__radio
    def area(self):
        return math.pi * self.__radio ** 2
    def __add__(self, otro_circulo):
        return Circulo( self.__radio + otro_circulo.__radio )


c1 = Circulo(4)
print(c1.getRadio())

c2 = Circulo(5)
print(c2.getRadio())

c3 = c1 + c2
print(c3.getRadio())
