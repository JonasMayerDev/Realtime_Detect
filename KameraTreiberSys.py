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

import sys,time

syspath0=sys.path[0]
exec(open(sys.path[0]+"/../../../../VirtualPython3/bin/activate_this.py").read(), {'__file__': sys.path[0]+"/../../../../VirtualPython3/bin/activate_this.py"})
sys.path.append(sys.path[0])
sys.path[0] = syspath0



import rospy,roslib
from sensor_msgs.msg import Image
""" 
from torchvision import transforms
import os
from PIL import Image
import numpy as np
import torch
from sensor_msgs.msg import Image as imageMsg
import torch.nn as nn 
import torch.nn.functional as F
from torch.autograd import Variable
import torch.optim as optim
import sys
import timeit
"""
from cv_bridge import CvBridge, CvBridgeError
"""
import topic_names
import std_msgs

from torch import nn,optim,utils,exp,stack,autograd,save,load
from torchvision import transforms,models,datasets
import os
import time
from PIL import Image """

import cv2
 
capture = cv2.VideoCapture(0)
bridge = CvBridge()
rospy.init_node('VideoSysPublisher')
VideoRaw = rospy.Publisher('kamera_bilder', Image, queue_size=10)

for i in range(1000000):
     
    ret, frame = capture.read()
    image_message = bridge.cv2_to_imgmsg(frame, encoding="passthrough")
    VideoRaw.publish(image_message)
    #time.sleep(0.1)
    #print(frame)
     
 
capture.release()
cv2.destroyAllWindows()
