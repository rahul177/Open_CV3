# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:23:54 2019

@author: Rahul Kumar
"""

import cv2
import numpy as np

# Load Image
image=cv2.imread('C:\\Users\\Rahul Kumar\\Desktop\\computer vision\\MasterOpenCV\\Master OpenCV\\images\\bunchofshapes.jpg')
cv2.imshow('Original Image',image)
cv2.waitKey(0)

# Create a black image with same dimensions as our loaded image
black_image=np.zeros((image.shape[0],image.shape[1],3))

#Create a copy of our original image
original_image=image

# Gray Scale our image
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Find Canny Edges
edged=cv2.Canny(gray,50,200)
cv2.imshow('Canny Edges',edged)
cv2.waitKey(0)

# Find Contour and print how many were found
contours,hierarchy=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print("Number of Contours found : ",len(contours))
"""
# Draw all contours
cv2.drawContours(black_image,contours,-1,(0,255,0),3)
cv2.imshow('Contour Draw over Black Image',black_image)
cv2.waitKey(0)

"""

# Draw all contours over image
cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imshow('All Contours',image)
cv2.waitKey(0)

cv2.destroyAllWindows()

############### SORTING BY AREA ####################
def get_contour_areas(contours):
    # Return area of all contours as list
    all_areas=[]
    for cnt in contours:
        area=cv2.contourArea(cnt)
        all_areas.append(area)
        
    return all_areas

print("Contour area before sorting", get_contour_areas(contours))

# Sort Contours Large to small
sorted_contours=sorted(contours,key=cv2.contourArea,reverse=True)

print("Contour area after sorting",get_contour_areas(sorted_contours))

# Iterative over our contours and draw one at a time
for c in sorted_contours:
    cv2.drawContours(original_image,[c],-1,(255,0,0),3)
    cv2.waitKey(0)
    cv2.imshow("Contours by area",original_image)
    
cv2.waitKey(0)
cv2.destroyAllWindows()





























