# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:13:52 2019

@author: macabre
"""

from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import matplotlib.pyplot as plt
#
def ejecucion(archivo):
    return runfile (archivo)
#
archivos=['grabaaudio.py','generadortonos.py']
#

# create a thread pool of 4 threads
with PoolExecutor(max_workers=4) as executor:

    # _ is the body of each page that I'm ignoring right now
    for _ in executor.map(ejecucion, archivos):
        pass
    
audio = np.frombuffer(b''.join(frames),dtype=np.int16) 
t = np.linspace(0,RECORD_SECONDS,num=audio.size)
plt.plot(t,audio)
plt.xlabel('Tiempo [s]')
plt.ylabel('Cuentas')
plt.grid()    
plt.show()
plt.xlim((5.00, 5.20))
print(min(audio[t>6]) , max(audio[t>6]))

plt.figure(2)
vppval=1.999
audiocorr= audio*vppval/(2*2**15)
t = np.linspace(0,RECORD_SECONDS,num=audiocorr.size)
plt.plot(t,audiocorr)
plt.xlabel('Tiempo [s]')
plt.ylabel('Volt')
plt.grid()    
plt.show()    
print(min(audiocorr[t>6]) , max(audiocorr[t>6]))
print(-min(audiocorr[t>6]) + max(audiocorr[t>6]))



import scipy.io.wavfile
scipy.io.wavfile.write('archivo.wav', 44100, audio)