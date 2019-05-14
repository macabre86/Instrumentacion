# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:42:42 2019

@author: macabre
"""

from lantz import MessageBasedDriver, Feat
from lantz.core import mfeats

class Osci (MessageBasedDriver):
    @Feat
    def idn(self):
        return self.query('*IDN?')
    
    def set_frequency(self,freq):
        self.write('dasa {}'.format(freq))
        
        
#osci=Osci('USb::0x0699::0x0363::X065092::INSTR')

osci= Osci.via_usb('C065092')
osci.inialize()
print(osci.idn)
        
        