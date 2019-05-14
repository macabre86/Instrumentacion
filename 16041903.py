# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:36:37 2019

@author: macabre
"""

def deco(func):
    def inner(x):
        print (func,x)
        return(func(x))
    return inner    

@deco                           #El decorador va con la funcion
def fun(x):
    print('fun')
    return 2*x

print(fun(3))

#Si se le quiere agregar funcionalidad que se llama decorador