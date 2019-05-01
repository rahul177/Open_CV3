# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:33:38 2019

@author: Rahul Kumar
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('C:\\Users\\Rahul Kumar\\Downloads\\IMG_20160918_200315.jpg')

# Transformation : 

height,width=image.shape[:2]
quarter_height,quarter_width=height/4,width/4
T=np.array([[1,0,quarter_width],[0,1,quarter_height]])
img_translation=cv2.warpAffine(image,T,(width,height))
cv2.imshow("Translation Image",img_translation)
cv2.waitKey()
cv2.destroyAllWindows()

# Rotation
rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),90,1)
rotated_image=cv2.warpAffine(image,rotation_matrix,(width,height))
cv2.imshow("Rotated Image",rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

# Resizing 
image_scaled=cv2.resize(image,None,fx=0.75,fy=0.75)
cv2.imshow("Linear Transpolation",image_scaled)
cv2.waitKey()

image_scaled=cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Cubic Transpolation",image_scaled)
cv2.waitKey()

image_scaled=cv2.resize(image,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow("Skewed Size",image_scaled)
cv2.waitKey()

cv2.destroyAllWindows()

# Image Pyramid

smaller_img=cv2.pyrDown(image)
bigger_img=cv2.pyrUp(image)
cv2.imshow("Smaller Image",smaller_img)
cv2.imshow("Bigger Image",bigger_img)
cv2.waitKey()
cv2.destroyAllWindows()

# Cropping

start_row,start_col=int(height*0.25),int(width*0.25)
end_row,end_col=int(height*0.75),int(width*0.75)
cropped=image[start_row:end_row,start_col:end_col]
cv2.imshow("Original Image",image)
cv2.imshow("Cropped Image",cropped)
cv2.waitKey()
cv2.destroyAllWindows()

# Arithmatic Operation for inc. or dec. brightness

M=np.ones(image.shape,dtype="uint8")*75
added=cv2.add(image,M)
cv2.imshow("Increase Brightness",added)

subtracted=cv2.subtract(image,M)
cv2.imshow("Decrease Brightness",subtracted)

cv2.waitKey()
cv2.destroyAllWindows()


# Masking
square=np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-2)
cv2.imshow("Square",square)
cv2.waitKey()

ellipse=np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("Ellipse",ellipse)
cv2.waitKey()

cv2.destroyAllWindows()


And=cv2.bitwise_and(square,ellipse)
cv2.imshow("AND",And)
cv2.waitKey()

Or=cv2.bitwise_or(square,ellipse)
cv2.imshow("OR",Or)
cv2.waitKey()

Xor=cv2.bitwise_xor(square,ellipse)
cv2.imshow("XOR",Xor)
cv2.waitKey()

Not=cv2.bitwise_not(square)
cv2.imshow("NOT",Not)
cv2.waitKey()

cv2.destroyAllWindows()

# Blurring 

cv2.imshow("Original Image",image)
cv2.waitKey()

kernel_3X3=np.ones((3,3),np.float32)/9
blurred=cv2.filter2D(image,-1,kernel_3X3)
cv2.imshow('3*3 Kernel Blurring',blurred)
cv2.waitKey()

kernel_7X7=np.ones((7,7),np.float32)/49
blurred=cv2.filter2D(image,-1,kernel_7X7)
cv2.imshow('7*7 Kernel Blurring',blurred)
cv2.waitKey()

cv2.destroyAllWindows()

# Thresholding
image_gray=cv2.imread('C:\\Users\\Rahul Kumar\\Downloads\\IMG_20160918_200315.jpg',0)
cv2.imshow('Original',image_gray)

ret,thresh1=cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thresh1)

cv2.waitKey()
cv2.destroyAllWindows()


# Dilation, Erosion, Opening and Closing
image_gray=cv2.imread('C:\\Users\\Rahul Kumar\\Downloads\\IMG_20160918_200315.jpg',0)
cv2.imshow('Original',image_gray)

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(image_gray,kernel,iterations=1)
cv2.imshow('Erosion',erosion)
cv2.waitKey()

dilation=cv2.dilate(image_gray,kernel,iterations=1)
cv2.imshow('Dilation',dilation)
cv2.waitKey()

opening=cv2.morphologyEx(image_gray,cv2.MORPH_OPEN,kernel)
cv2.imshow('Opening',opening)
cv2.waitKey()

closing=cv2.morphologyEx(image_gray,cv2.MORPH_CLOSE,kernel)
cv2.imshow('Closing',closing)
cv2.waitKey()

cv2.destroyAllWindows()

# Edge Deteection and Image Gradient

image_gray=cv2.imread('C:\\Users\\Rahul Kumar\\Downloads\\IMG_20160918_200315.jpg',0)
cv2.imshow('Original',image_gray)
cv2.waitKey()

"""
sobel_x=cv2.Sobel(image_gray,cv2.CV_64F,0,1,ksize=5)
sobel_y=cv2.Sobel(image_gray,cv2.CV_64F,1,0,ksize=5)
cv2.imshow('Horizontal Edge',sobel_x)
cv2.waitKey()

cv2.imshow('Vertical Edge',sobel_y)
cv2.waitKey()

sobel_OR=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Combine Edge',sobel_OR)
cv2.waitKey()

laplacian=cv2.Laplacian(image_gray,cv2.CV_64F)
cv2.imshow('Laplacian',laplacian)
cv2.waitKey()
"""


canny=cv2.Canny(image_gray,50,170)
cv2.imshow('Canny',canny)
cv2.waitKey()

cv2.destroyAllWindows()















































