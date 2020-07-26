# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:20:52 2020

@author: chintan
"""


import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier('C:/Users/chintan/Downloads/haarcascade_frontalface_default.xml')
img=cv2.imread('C:/Users/chintan/Desktop/College/IMG-20190128-WA0061.jpg',1)

faces=face_cascade.detectMultiScale(img,1.5,3)
print(faces)

for(x,y,w,h) in faces:
    print(x,y,w,h)
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),5)
    
resized=cv2.resize(img,(500,500))
cv2.imshow('img',img)
cv2.imshow('img',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()    