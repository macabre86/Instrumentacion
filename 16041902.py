# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:23:51 2019

@author: macabre
"""

class MiClase:
    def __init__(self,value):
        self._value=value

#Si quiero que sea privada
#        self._value=value
#        
    def get_value(self):
        return self._value

    def set_value(self,value):
        if not isinstance(value,float):
            raise ValueError
        self._value=value     
    
    value= property(get_value,set_value)    #A este atributo que conecta con un getter y un setter

#El descriptor/propiedad que se conecta (variable) a la que se cambia el valor o se lee a partir de un metodo
# Hqy que adicionar metodos.
        
c=MiClase(8)
c.value=8.0
print(c.value)



#LA forma con decorador


class MiClase:
    def __init__(self,value):
        self._value=value

#Si quiero que sea privada
#        self._value=value
    @property   #lo que sigue es el getter de value    
    def value(self):
        return self._value
    
    @value.setter #Lo que sigue es el seter de value
    def value(self,value):
        if not isinstance(value,float):
            raise ValueError
        self._value=value     
    
 #El descriptor/propiedad que se conecta (variable) a la que se cambia el valor o se lee a partir de un metodo
# Hqy que adicionar metodos.
        
c=MiClase(8)
c.value=8.0
print(c.value)
