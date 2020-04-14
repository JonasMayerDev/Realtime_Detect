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
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton,QSlider,QComboBox
from PyQt5 import uic
sys.path.append(sys.path[0]+"/../Realtime_Detect/QtGui")
import Finishwindow 
FinishWindow = Finishwindow.Finishwindow()

class Launchwindow:
    
    def __init__(self):
        self.Launchwindow = uic.loadUi(sys.path[0]+"/../Realtime_Detect/QtGui/Launchwindow.ui")

        self.lineEditName = self.Launchwindow.lineEditName
        self.pushButtonSave = self.Launchwindow.pushButtonSave
        self.comboBoxModel = self.Launchwindow.comboBoxModel
        self.doubleSpinBoxSchwelle = self.Launchwindow.doubleSpinBoxSchwelle
        self.pushButtonWeiter = self.Launchwindow.pushButtonWeiter
        self.radioButtonSysKam = self.Launchwindow.frame.findChild(QRadioButton,"radioButton1")
        self.comboBoxSysKam = self.Launchwindow.frame.findChild(QComboBox,"comboBox_2")
        self.pushButtonSave.setText("Save Name")

        matching = [s for s in os.listdir("/dev") if "video" in s]
        for i in matching:
            if i.find("video")==0:
                self.comboBoxSysKam.addItem(i)

        models = os.listdir(sys.path[0]+"/../Models")
        for i in models:
            self.comboBoxModel.addItem(i)


        def lock_name():
            #print(dir(self.buttonName))
            if self.pushButtonSave.text() == "Save Name":
                
                self.lineEditName.setEnabled(False)
               
                self.pushButtonSave.setText("Edit Name")
                self.wasNameSet = True
            else:
                self.lineEditName.setEnabled(True)
                #TODO check if alredy exist!
                
                self.pushButtonSave.setText("Save Name")
                self.wasNameSet = False

        self.pushButtonSave.clicked.connect(lock_name)
        self.pushButtonWeiter.clicked.connect(self.weiter)
    

    def weiter(self):
        try:
            modelname = self.comboBoxModel.itemText(self.comboBoxModel.currentIndex())
        except:
            modelname = ""
            print("Please select an Model") 

        try:
            KNum = self.comboBoxSysKam.itemText(self.comboBoxSysKam.currentIndex())[5:]
            print(KNum)
            int(KNum)
        except:
            KNum = ""
            print(KNum)
            print("Please connect an Kamera and make shure its appearing in /dev ant it follows the rule: videoNUMBER") 


        if modelname == "" or not self.wasNameSet or KNum == "":

            print("Failed: please retry ")

        else:

            if "ros_ws" in os.listdir(sys.path[0]+"/.."):
                print("contin")
            else:
                self.create_ros_ws()
                self.create_ros_pack()
                self.move_files_in_pack()
                self.source_all()
            if not "launch" in os.listdir(sys.path[0]+"/../ros_ws/src/realtime_detect"):
                os.system("mkdir "+sys.path[0]+"/../ros_ws/src/realtime_detect/launch")
            
            self.create_launchfile()
            FinishWindow.Finishwindow.show()
            self.Launchwindow.close()



    def create_ros_ws(self):
        path = sys.path[0]+"/.."
        cmd = """mkdir -p """+path+"""/ros_ws/src &&
                cd """+path+"""/ros_ws/ &&
                . """+path+"""/VirtualPython3/bin/activate &&
                export PYTHONPATH=:$PYTHONPATH:"""+path+"""/VirtualPython3/lib/python3.6/site-packages &&
                catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3 &&
                . """+path+"""/ros_ws/devel/setup.sh &&
                echo $ROS_PACKAGE_PATH """

        anwser = os.popen(cmd)
        print(anwser)
        if "not found" in anwser:
            print("Seams like catkin is not installed")
            return -1

        #TODO test awnser if worked


    def create_ros_pack(self):
        path = sys.path[0]+"/.."
        cmd = """. /opt/ros/melodic/setup.sh    &&
                export PYTHONPATH=:$PYTHONPATH:"""+path+"""/VirtualPython3/lib/python3.6/site-packages &&
                . """+path+"""/ros_ws/devel/setup.sh &&
                cd """+path+"""/ros_ws/src &&
                catkin_create_pkg realtime_detect std_msgs rospy roscpp cv_bridge message_generation roslib &&
                cd """+path+"""/ros_ws &&
                catkin_make &&
                . """+path+"""/ros_ws/devel/setup.sh """

        anwser = os.popen(cmd)
        print(anwser)
        if "not found" in anwser:
            print("Seams like catkin is not installed")
            return -1
        else:
            return 0
        #TODO test awnser if worked


    def move_files_in_pack(self):
        path = sys.path[0]+"/../Realtime_Detect"
        path2 = sys.path[0]+"/.."
        cmd ="""chmod 700 """+path+"""/Bilderkennung.py &&
                chmod 700 """+path+"""/KameraTreiberSys.py &&
                chmod 700 """+path+"""/topic_names.py &&
                cp """+path+"""/topic_names.py """+path2+"""/ros_ws/src/realtime_detect/src/topic_names.py &&
                cp """+path+"""/KameraTreiberSys.py """+path2+"""/ros_ws/src/realtime_detect/src/KameraTreiberSys.py &&
                cp """+path+"""/Bilderkennung.py """+path2+"""/ros_ws/src/realtime_detect/src/Bilderkennung.py"""
        anwser = os.popen(cmd)
        print(anwser)
    

    def source_all(self):
        path = sys.path[0]+"/.."
        cmd = """. /opt/ros/melodic/setup.sh    &&
                export PYTHONPATH=:$PYTHONPATH:"""+path+"""/VirtualPython3/lib/python3.6/site-packages &&
                . """+path+"""/ros_ws/devel/setup.sh &&
                cd """+path+"""/ros_ws &&
                catkin_make &&
                . """+path+"""/ros_ws/devel/setup.sh """
        anwser = os.popen(cmd)
        print(anwser)

    def create_launchfile(self):
        path2 = sys.path[0]+"/.."

        if self.radioButtonSysKam.isChecked():

            KNum = self.comboBoxSysKam.itemText(self.comboBoxSysKam.currentIndex())[5:]
            
            f = open(path2+"""/ros_ws/src/realtime_detect/launch/"""+self.lineEditName.text()+".launch", "a")
            f.write("""<?xml version="1.0"?> <launch> <rosparam param="kamera_number">"""+str(KNum)+"""</rosparam>
            <node name="KameraTreiberSys" pkg="realtime_detect" type="KameraTreiberSys.py"> </node> """)
            f.close()
        else: 
            print("something else than sys kam is not implmented")

        modelname = self.comboBoxModel.itemText(self.comboBoxModel.currentIndex())

        f = open(path2+"""/ros_ws/src/realtime_detect/launch/"""+self.lineEditName.text()+".launch", "a")
        f.write(""" <rosparam param="model_name">"""+str(modelname)+"""</rosparam> 
        <node pkg="realtime_detect" name="Bilderkennung" type="Bilderkennung.py" output="screen"> </node></launch>""")
        f.close()

        
        
        

        
        


