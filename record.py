#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, threading
import pyaudio, wave
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = "output4.wav"
RECORDING = False

def record_thread(fileName, stream, p):
    print('recording')
    waveFile = wave.open(fileName, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    while RECORDING:
        waveFile.writeframes(stream.read(CHUNK))
    waveFile.close()
    print('end')

def record_generator(fileName, recordBtn):
    global RECORDING
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
        channels=CHANNELS, \
        rate=RATE, \
        input=True, \
        input_device_index=1, \
        frames_per_buffer=CHUNK)
    while 1:
        recordBtn.setText(u'Start Recording')
        yield
        recordBtn.setText(u'Stop Recording')
        RECORDING = True
        t = threading.Thread(target=record_thread, args=(fileName, stream, p))
        t.setDaemon(True)
        t.start()
        yield
        RECORDING = False
