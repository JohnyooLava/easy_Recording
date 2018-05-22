#!/usr/bin/env python
#-*-coding:utf-8-*-
import wave
import pylab as pl
from Tkinter import *
from tkFileDialog import *
import numpy as np

# open wav file
Tk().withdraw()
file = askopenfilename(initialdir='easy_Recording')
wf = wave.open(file,'rb')

# read data
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = wf.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# read data of shape
str_data = wf.readframes(nframes)
wf.close()

# transform to array
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)


# plot the waveform
pl.subplot(211)
pl.plot(time, wave_data[0])
pl.xlabel("Channel 1")
pl.subplot(212)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("Channel 2")
pl.show()