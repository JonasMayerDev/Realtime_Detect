#!/usr/bin/env python3
import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton,QSlider
from PyQt5 import uic

class Finishwindow:
    
    def __init__(self):
        self.Finishwindow = uic.loadUi(sys.path[0]+"/../realtime_detect/QtGui/Finishwindow.ui")

        
        self.pushButtonBeenden = self.Finishwindow.pushButton
        self.pushButtonBeenden.clicked.connect(self.stop)
        
    def stop(self):
        self.Finishwindow.close()
        exit()
    
