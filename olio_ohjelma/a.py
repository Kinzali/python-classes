from b import B 

class A:
    def __init__ (self):
        self.numero = 0 # a.numero = 0
        olioB = b.B(self)
        olioB.muuta_numero()
        olioB.muuta_numero()
        olioB.muuta_numero()
        print(self.numero)
        #b.testaa()
        
        
    def muuta_numero(self):
        self.b.muuta_numero()
        
a = A()