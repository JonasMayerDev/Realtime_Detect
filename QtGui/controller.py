#!/usr/bin/env python3

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
