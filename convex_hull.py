# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:27:28 2019

@author: Rahul Kumar
"""
import cv2
import numpy as np

# Load image and keep copy

image=cv2.imread('C:\\Users\\Rahul Kumar\\Desktop\\computer vision\\MasterOpenCV\\Master OpenCV\\images\\hand.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image',image)
cv2.waitKey(0)

ret,thresh=cv2.threshold(gray,176,255,0)

contours,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

# Sort Contours by area and then remove the largest frame contour
n=len(contours)-1
contours=sorted(contours,key=cv2.contourArea,reverse=False)[:n]

# Iterate through contours and draw the convex hull

for c in contours:
    hull=cv2.convexHull(c)
    cv2.drawContours(image,[hull],0,(0,255,0),2)
    cv2.imshow('Convex Hull',image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()