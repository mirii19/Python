import abc
from abc import ABCMeta

class Vehiculo(metaclass=ABCMeta):
    __metaclass__= ABCMeta

    @abc.abstractmethod
    def quien_eres(self):
        print ("Soy un vehiculo y un metodo abstracto")

class coche(Vehiculo) :
    def quien_eres(self):
        print("Soy un coche")


coche = coche()
coche.quien_eres()
