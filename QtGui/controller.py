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

import sys,os
sys.path.insert(0,sys.path[0]+"/..")
syspath0=sys.path[0]
exec(open(sys.path[0]+"/../VirtualPython3/bin/activate_this.py").read(), {'__file__': sys.path[0]+"/../VirtualPython3/bin/activate_this.py"})
sys.path.append(sys.path[0])
sys.path[0] = syspath0
from PyQt5.QtWidgets import QApplication
app = QApplication(sys.argv)

import Launchwindow
import Checkwindow

LaunchWindow=Launchwindow.Launchwindow()
checkwindow = Checkwindow.Checkwindow()


def weiter_checkwindow():
    if checkwindow.allInstallesComplet:
        
        #choosewindow.Choosewindow.show()
        LaunchWindow.Launchwindow.show()
        checkwindow.Checkwindow.close()
    else:
        print("Warte bis die Installation <br>beendet ist!")


checkwindow.buttonWeiter.clicked.connect(weiter_checkwindow)
checkwindow.Checkwindow.show()

app.exec_()
