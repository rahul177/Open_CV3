# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:10:48 2019

@author: Rahul Kumar
"""

import cv2
import numpy as np

# Load image and keep copy

image=cv2.imread('C:\\Users\\Rahul Kumar\\Desktop\\computer vision\\MasterOpenCV\\Master OpenCV\\images\\house.jpg')
orig_image=image.copy()
cv2.imshow('Original Image',orig_image)
cv2.waitKey(0)

# Grayscale and binarize
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

# Find Contours
contours,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

# Iterate through each contour and compute the bounding rectangle
for c in contours:
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(orig_image,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Bounding Rectangle",orig_image)
    
cv2.waitKey(0)

# Iterate through each contour and compute the approx contour
for c in contours:
    #Calculate accuracy as percent of the contour perimeter
    accuracy=0.03*cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,accuracy,True)
    cv2.drawContours(image,[approx],0,(0,255,0),2)
    cv2.imshow('Approx Poly DP',image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()











