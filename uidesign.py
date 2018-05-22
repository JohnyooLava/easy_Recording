#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pyaudio
import wave
import record
import play
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('EasyRecording')
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        recordButton = QPushButton('Start Recording', self)
        recordButton.move(20, 10)
        recordButton.resize(300,200)
        g = record.record_generator('output3.wav', recordButton)
        g.__next__()
        recordButton.clicked.connect(lambda: g.__next__())

        playButton = QPushButton('Start Playing', self)
        playButton.move(600, 10)
        playButton.resize(300, 200)
        pl = play.play_generator(playButton)
        pl.__next__()
        playButton.clicked.connect(lambda: pl.__next__())
        self.show()

    #@pyqtSlot()
    #def playBtn(self):
    #    play.playBack()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=MyWindow()
    sys.exit(app.exec_())

