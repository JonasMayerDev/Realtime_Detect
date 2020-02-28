#!/usr/bin/env python3
import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QCheckBox,QRadioButton,QSlider
from PyQt5 import uic

class Launchwindow:
    
    def __init__(self):
        self.Launchwindow = uic.loadUi(sys.path[0]+"/../realtime_detect/QtGui/Launchwindow.ui")

        self.lineEditName = self.Launchwindow.lineEditName
        self.pushButtonSave = self.Launchwindow.pushButtonSave
        self.comboBoxModel = self.Launchwindow.comboBoxModel
        self.doubleSpinBoxSchwelle = self.Launchwindow.doubleSpinBoxSchwelle
        self.pushButtonWeiter = self.Launchwindow.pushButtonWeiter
        self.radioButtonSysKam = self.Launchwindow.frame.findChild(QRadioButton,"radioButton1")
        self.comboBoxSysKam = self.Launchwindow.frame.findChild(QRadioButton,"comboBox_2")


        self.pushButtonSave.setText("Save Name")

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
        if "ros_ws" in os.listdir(sys.path[0]+"/.."):
            print("contin")
        else:
            self.create_ros_ws()
            self.create_ros_pack()
            self.move_files_in_pack()
            self.source_all()



    def create_ros_ws(self):
        path = sys.path[0]+"/.."
        cmd = """mkdir -p """+path+"""/ros_ws/src &&
                cd """+path+"""/ros_ws/ &&
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
        path = sys.path[0]+"/../realtime_detect"
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
                . """+path+"""/ros_ws/devel/setup.sh &&
                cd """+path+"""/ros_ws &&
                catkin_make &&
                . """+path+"""/ros_ws/devel/setup.sh """
        anwser = os.popen(cmd)
        print(anwser)
        
        


