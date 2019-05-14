# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:24:15 2019

@author: macabre
"""

import pyaudio
import numpy as np
import matplotlib



CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 0.1
WAVE_OUTPUT_FILENAME = "output.wav"
 
p = pyaudio.PyAudio()
'''
print("Input Device Info")
print(p.get_default_input_device_info())
print("Output Device Info")
print(p.get_default_output_device_info())
 
for i in range(p.get_host_api_count()):
    print(p.get_host_api_info_by_index(i))
'''
for index in range(p.get_device_count()):
    print(p.get_device_info_by_index(index))
 
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=0)
 
print("* recording")
 
frames = []
 
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
 
 
print("* done recording")
 
stream.stop_stream()
stream.close()
p.terminate()
 
time = []
 
 
audio = np.fromstring(b''.join(frames),dtype=np.int16)
 
t = np.linspace(0,RECORD_SECONDS,num=audio.size)
import matplotlib.pyplot as plt
plt.plot(t,audio)
plt.show()



