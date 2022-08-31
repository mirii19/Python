from zope.interface import Interface, Attribute, implements
class IFoo(Interface):
    def saludo():
       print "Hola"


class Foo(object):
    implements(IFoo)
    def __init__(self, otro="Mundo"):
        self.otro = otro

    def saludo(self):
        print "Hola", self.otro


saludo = Foo()
saludo.saludo()
