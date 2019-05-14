# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:48:50 2019

@author: macabre
"""


from lantz import Feat
from lantz.messagebased import MessageBasedDriver
from lantz import Feat, DictFeat
import matplotlib.pyplot as plt


class LantzSignalGenerator(MessageBasedDriver):
    """Lantz Signal Generator
    """

    DEFAULTS = {'COMMON': {'write_termination': '\n',
                           'read_termination': '\n'}}


    def query(self, command, *, send_args=(None, None), recv_args=(None, None)):
        answer = super().query(command, send_args=send_args, recv_args=recv_args)
        if answer == 'ERROR':
            raise InstrumentError
        return answer

    @Feat()
    def idn(self):
        return self.query('?IDN')

    @Feat(units='V', limits=(10,))
    def amplitude(self):
        """Amplitude.
        """
        return float(self.query('?AMP'))

    @amplitude.setter
    def amplitude(self, value):
        self.query('!AMP {:.1f}'.format(value))

    @Feat(units='V', limits=(-5, 5, .01))
    def offset(self):
        """Offset.
        """
        return float(self.query('?OFF'))

    @offset.setter
    def offset(self, value):
        self.query('!OFF {:.1f}'.format(value))

    @Feat(units='Hz', limits=(1, 1e+5))
    def frequency(self):
        """Frequency.
        """
        return float(self.query('?FRE'))

    @frequency.setter
    def frequency(self, value):
        self.query('!FRE {:.2f}'.format(value))

    @Feat(values={True: 1, False: 0})
    def output_enabled(self):
        """Analog output enabled.
        """
        return int(self.query('?OUT'))

    @output_enabled.setter
    def output_enabled(self, value):
        self.query('!OUT {}'.format(value))

    @Feat(values={'sine': 0, 'square': 1, 'triangular': 2, 'ramp': 3})
    def waveform(self):
        return int(self.query('?WVF'))

    @waveform
    def waveform(self, value):
        self.query('!WVF {}'.format(value))

if __name__ == '__main__':
    from time import sleep
    from lantz import Q_
    from lantz.log import log_to_screen, DEBUG

    volt = Q_(1, 'V')
    milivolt = Q_(1, 'mV')
    Hz = Q_(1, 'Hz')

    log_to_screen(DEBUG)
    with LantzSignalGenerator('TCPIP::localhost::5678::SOCKET') as inst:
        print('The identification of this instrument is : ' + inst.idn)
        print('Setting amplitude to 3')
        inst.amplitude = 3 * volt
        inst.offset = 200 * milivolt
        inst.frequency = 20 * Hz
        inst.output_enabled = True
        inst.waveform = 'sine'


