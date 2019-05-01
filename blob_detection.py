# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:22:50 2019

@author: Rahul Kumar
"""

import cv2
import numpy as np

image = cv2.imread('C:\\Users\\Rahul Kumar\\Desktop\\computer vision\\MasterOpenCV\\Master OpenCV\\images\\Sunflowers.jpg',0)

detector=cv2.SimpleBlobDetector()
keypoints=detector.detect(image)

blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(image,keypoints,blank,(0,255,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blobs",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()


