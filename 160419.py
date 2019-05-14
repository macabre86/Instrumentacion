# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:19:28 2019

@author: macabre
"""

#Explica hoy las instancias de error.

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:54:43 2019

@author: macabre
"""
from math import pi

class Forma:
    def ratio(self):
        return self.area()/self.perimetro() 

class Circulo:
    def  __init__(self,radio):
        self.radio=radio
    def area(self):
        return pi*self.radio*self.radio
    def perimetro(self):
        return pi*2*self.radio
    def ratio(self):
        return self.area()/self.perimetro()       
    
class Cuadrado:
    def __init__(self,lado):
        self.lado=lado
    def area(self):
        return self.lado*self.lado
    def perimetro(self):
        return 4*self.lado
    def ratio(self):
        return self.area()/self.perimetro()

    
cir=Circulo(3)
print(cir.area(),cir.perimetro(),cir.ratio())

#Propieades
#LA variable asociada al objeto se llama atributo

#Puedo agregar atributos despues de formar la clase








