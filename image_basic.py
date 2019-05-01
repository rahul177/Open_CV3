# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:08:17 2019

@author: Rahul Kumar
"""

import cv2
import numpy as np
image=cv2.imread('C:\\Users\\Rahul Kumar\\Desktop\\New Doc 2019-02-08 20.00.04_1.jpg')
cv2.imshow("Coloured Image",image)
cv2.waitKey()

grey_image=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image",grey_image)
cv2.waitKey()

cv2.destroyAllWindows()


# Histogram 
import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('C:\\Users\\Rahul Kumar\\Desktop\\New Doc 2019-02-08 20.00.04_1.jpg')
histogram=cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256])
plt.show()
color=('b','g','r')
for i,col in enumerate(color):
    histogram2=cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram2,color=col)
    plt.xlim([0,256])
    
plt.show()

# Drawing Images and Shapes using OpenCV

# Making a black square
import cv2
import numpy as np
image=np.zeros((512,512,3),np.uint8)

image_bw=np.zeros((512,512),np.uint8)
cv2.imshow("Black Rectangle (Color)",image)
cv2.imshow("Black Rectanngle (B&W)",image_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Line Draw 
image=np.zeros((512,512,3),np.uint8)
cv2.line(image,(0,0),(500,500),(255,0,0),5)
cv2.imshow("Blue Line",image)
cv2.waitKey()
cv2.destroyAllWindows()

# Rectangle
cv2.rectangle(image,(20,20),(100,100),(0,255,0),-1)
cv2.imshow('Green Rectangle',image)
cv2.waitKey()
cv2.destroyAllWindows()

# Ploygon 
pts=np.array([[10,50],[400,50],[90,200],[50,500]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(0,0,255),3)
cv2.imshow("Polygon Red",image)
cv2.waitKey()
cv2.destroyAllWindows()

# Put Text on Image
cv2.putText(image,'Hello World',(75,290),cv2.FONT_HERSHEY_COMPLEX,2,(255.255,23),3)
cv2.imshow("Hello World",image)
cv2.waitKey()
cv2.destroyAllWindows()




















