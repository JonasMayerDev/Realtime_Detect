#!/usr/bin/env python3
import sys

syspath0=sys.path[0]
exec(open(sys.path[0]+"/../../../../VirtualPython3/bin/activate_this.py").read(), {'__file__': sys.path[0]+"/../../../../VirtualPython3/bin/activate_this.py"})
#exec(open(sys.path[0]+"/VirtualPython3/bin/activate_this.py").read(), {'__file__': sys.path[0]+"/VirtualPython3/bin/activate_this.py"})
sys.path.append(sys.path[0])
sys.path[0] = syspath0
sys.path.insert(0,sys.path[0]+"/../../../../VirtualPython3/lib/python3.6/dist-packages")

import rospy,roslib
import cv2
from cv2 import *
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
from cv_bridge import CvBridge, CvBridgeError
import topic_names
import std_msgs

from torch import nn,optim,utils,exp,stack,autograd,save,load
from torchvision import transforms,models,datasets
import os
import time
from PIL import Image

rospy.init_node("bilderkennung_ki")
normalize = transforms.Normalize(
    mean=[0.485,0.456,0.406],
    std=[0.229,0.224,0.225]
)

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(256),
    transforms.ToTensor(),
    normalize
])

if rospy.has_param("/model_name"):
    model_name = rospy.get_param("/model_name")
    path = sys.path[0]+"/../../../../Models/"+model_name+"/"
    #path = sys.path[0]+"/Models/"
    try:
        modelUClasses = torch.load(path+model_name+".pt")
        print(modelUClasses)
    except FileNotFoundError:
        model = models.vgg16(pretrained=True)
        print("model wurde mit namen",'"'+model_name+'"',"wurde noch nicht erstellt.\n Bitte schaue hier nach deinem Model",path+model_name+".pt")
    model = modelUClasses["model"]
    classes = modelUClasses["classes"]
    model.eval()

else :
    print("Rosparam /model_name not set")

outWrite = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))
i = 0
def image_callback(image):
    global i
    global outWrite
    i +=1
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image, desired_encoding="passthrough")
    
    imageData = transform(Image.fromarray(cv_image)) #to bring it in form 1*3*255*255
    inpt=torch.Tensor(imageData.unsqueeze(0))
    inpt = Variable(inpt)
    out = model(inpt)
    out = torch.exp(out)
    namenTest=[]
    prop = 0.5
    for i in range(len(out)):
            a =0
            for proz in out[i]:
                if float(proz)>0.8:
                    namenTest.append(classes[a])
                    prop = proz
                a=a+1
    if len(namenTest) == 0:
        namenTest.append("None")
    classifiedName_pub.publish(namenTest[0])
    print("Das erkannte Objekt ist: ["+str(namenTest[0])+"] mit einer Wahrscheinlichkeit von "+str(int(prop*100.0))+"% \n",out[i],classes)
    if i > 400:
        outWrite.release()
    else:
        outWrite.write(cv_image)
classifiedName_pub = rospy.Publisher(topic_names.classified_name_topic(), std_msgs.msg.String, queue_size=10)


rospy.Subscriber(topic_names.raw_image_topic(),imageMsg,image_callback)

while not rospy.core.is_shutdown():
    rospy.rostime.wallsleep(0.5)
""" try:
    
    model.load_state_dict(load("/home/jonas/git/sfz_cvb/Models/testGolf2.pt"))
except:
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(),lr=0.0001)

    def trainClassifier():
        epochs = 30
        steps = 0

        for e in range(epochs):

            model.train()

            for image,label in iter(trainImages):

                steps +=1
                optimizer.zero_grad()
                output = model.forward(image)
                print(output.size())
                loss = criterion(output,label)
                loss.backward()
                optimizer.step()
                print(str(loss.data)+" ev "+str(e))

    trainClassifier()
    save(model.state_dict(),"testsave.pt")
for images,labels in iter(testImages):
    output = model.forward(images)
    print(output.size())
    output = exp(output)
    print("Der Output ist: "+str(output)+" und sollte das sein: "+str(labels))


i=2
while i <= 13:
    array = []
    Img = Image.open("/home/jonas/Schreibtisch/PicsKiGolfHell/"+"Test"+str(i)+".jpeg")
    array.append(transformTest(Img))
    print("start")
    out=model(autograd.Variable(stack(array)))
    print(output.size())
    out = exp(out)
    print("end")
    a =0
    name="none"
    print(out[0])
    for proz in out[0]:
        if float(proz)>0.8:
            name=classes[a]
        
        a=a+1
    
    Img.show()
    print(name)
    time.sleep(5)
    i=i+1 """
