# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:50:37 2019

@author: Rahul Kumar
"""

import cv2
import numpy as np

image=cv2.imread('C:\\Users\\Rahul Kumar\\Desktop\\computer vision\\MasterOpenCV\\Master OpenCV\\images\\shapes.jpg')
cv2.imshow("Input Image",image)
cv2.waitKey(0)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged=cv2.Canny(gray,30,200)

cv2.imshow('Canny Edges',edged)
cv2.waitKey(0)

contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Egdes After Contouring',edged)
cv2.waitKey(0)

print("Number of Contours found = " +str(len(contours)))

cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imshow('Contours',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

















