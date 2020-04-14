#!/usr/bin/env python3

#AI_Model_Creator; an easy to use AI cumputer vision model creator.
#Copyright (C) 2020  Jonas Mayer

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by    
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#You can contact me by mail: bysuxaxofficial@gmail.com

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton
from PyQt5 import uic
from PyQt5.QtCore import QThread, QObject,pyqtSignal


#progressBarInstall = None
checkBoxROS = None


class Installer(QObject):
    progressBarInstall = pyqtSignal(int)
    
    def startInstalling(self):
        global checkBoxROS

        self.progressBarInstall.emit(1)

        if checkBoxROS.isChecked():
            answerRos=os.system("/bin/bash "+sys.path[0]+"/../Realtime_Detect/"+"InstallRos.bash "+sys.path[0]+"/..")
            self.progressBarInstall.emit(50)
            awnserRosVP3=os.system("/bin/bash "+sys.path[0]+"/../Realtime_Detect/"+"InstallRosVP3.bash "+sys.path[0]+"/..")
        else: 
            print("Bitte wählen sie eine Option")
        self.progressBarInstall.emit(100)
        


class Checkwindow:
    
    def __init__(self):
        
        global checkBoxROS

        self.Checkwindow = uic.loadUi(sys.path[0]+"/../Realtime_Detect/QtGui/Checkwindow.ui")
        self.buttonAutoInstall = self.Checkwindow.pushButtonAuto
        self.buttonManuelInstall = self.Checkwindow.pushButtonManuel
        self.buttonWeiter = self.Checkwindow.pushButtonWeiter
        self.progressBarInstall =  self.Checkwindow.progress_bar

        checkBoxROS = self.Checkwindow.frame_2.findChild(QCheckBox,"check_box_ros")
        checkBoxROS.setEnabled(False)
        
        self.allInstallesComplet = True

        def update_progressbar(val):
            self.progressBarInstall.setValue(val)
            if val == 100:
                self.allInstallesComplet = True
            else:
                self.allInstallesComplet = False


        def test():
            self.buttonAutoInstall.setVisible(False)
            self.progressBarInstall.setVisible(True)
            self.progressBarInstall.setValue(0)
            self.obj = Installer()  #starte nebenprocesse 
            self.obj.progressBarInstall.connect(update_progressbar)
            self.thread = QThread()  
            self.obj.moveToThread(self.thread)
            self.thread.started.connect(self.obj.startInstalling)    
            self.thread.start()

            
        
        self.progressBarInstall.setVisible(False)
        self.buttonAutoInstall.clicked.connect(test)
        


    
    
        #print(dir(checkBoxUseKamera))
