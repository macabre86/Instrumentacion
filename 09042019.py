# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:20:45 2019

@author: macabre
"""

def duplicar(lista):
    y=[]
    for elemento in lista:
        y.append(2*elemento)
    return y

#Esto no esta bueno por que iterea sobre la lista y python lo hace facil
    
def duplicar_horrible(lista):
    y=[]
    for n in range(len(lista)):
        y.append(2*lista[n])
    return y

#No solo funciona para listas , sino a cosas compatibles con este patron (iterable)

x=[1,2,3] 
print(x)    
print(duplicar(x))

#Si hay algo que tiene que ser recordado , Clases de python

class MiLista:
    def __init__(self,contenido):
        self.contenido=contenido  #Agregar un atributo que se llama contenido
    def duplicar(self):
        y=[]
        for elemento in self.contenido:
            y.append(2*elemento)
        return y
    def __len__(self):
        return len(self.contenido)

x=MiLista([1,2,3])  #Llamo al constructor del objeto, o sea al init
print(x.duplicar()) # el x. pasa como el argumento de la funcion duplicar
print(x.__len__())