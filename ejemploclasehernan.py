# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:17:11 2019

@author: macabre
"""
import visa
rm=visa.ResourceManager()



class OsciloscopioTDS1002b:   #si no hay nada , es clase objeto
    
    def __init__(self,serialno):
        self.serialno=serialno      
        self.inst=rm.open_resource('USB::0x0645:0x0313::{}::INSTR'.format(serialno))
        #Hacer algo
     def idn(self)
         return self.inst.query('IDN?')
        
     def set_timebase(self,seconds):
         self.inst.write('HOR:DEL:SCA {}'.format(seconds))   #escala del eje
        
    
class GeneradorFunciones:
    

#Que quiero    
osci=Osciloscopio('C01231')   "Pasarle el numero de serie
print(osci.idn())
osci.set_timebase(10)
osci.set_scale(10)
out=osci.get_channel(1)

gen=GeneradorFunciones('23123123')
print(gen.idn())
gen.set_shape('sin')
gen.set_amplitude(5)
gen.set_frequency(15)    