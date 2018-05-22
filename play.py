#!/usr/bin/env python
#-*-coding:utf-8-*-
import pyaudio
import wave
import threading
import sys
import tkinter as tk
from tkinter import filedialog

CHUNK = 1024
def play_generator(playBtn):
    global PLAYING

    while 1:
        playBtn.setText(u'Start Playing')
        yield
        playBtn.setText(u'Stop Playing')

        root = tk.Tk()
        root.withdraw()
        file = filedialog.askopenfilename(initialdir='easy_Recording')
        wf = wave.open(file, 'rb')
        # instantiate PyAudio
        p = pyaudio.PyAudio()

        # open stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), \
                        channels=wf.getnchannels(), \
                        rate=wf.getframerate(), \
                        output=True)

        PLAYING = True
        t = threading.Thread(target=play_thread, args=(wf, stream, p))
        t.setDaemon(True)
        t.start()

        yield
        PLAYING = False

def play_thread(wf, stream, p):
    print('playing')
    # read data
    data = wf.readframes(CHUNK)
    while PLAYING:
        # play stream
        # while (len(data) > 0):
        stream.write(data)
        data = wf.readframes(CHUNK)
    # stop stream
    stream.stop_stream()
    stream.close()
    # close PyAudio
    p.terminate()
    print('end')


