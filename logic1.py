import numpy as np 
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')
#SIMPLE ADDITION
#add = img1 +img2

#WITH CV2 ADDITION
#add = img1 + img2

#WITH WEIGHTED ADDITION OF IMAGES
#with image and opacity and then finally gamma value
#weighted = cv2.addWeighted(img1 , .6 , img2 , .4 , 0)

rows,cols,channels = img3.shape
roi = img1[0:rows , 0:cols]
img2gray = cv2.cvtColor(img3 , cv2.COLOR_BGR2GRAY)
#CREATING THE THRESOLD IMAGE
ret , mask = cv2.threshold(img2gray , 220 , 255 , cv2.THRESH_BINARY_INV)
#for inverse of mask
mask_inv = cv2.bitwise_not(mask)
img1_bg  = cv2.bitwise_and(roi,roi, mask = mask_inv)
img3_fg  = cv2.bitwise_and(img3 , img3 ,mask=mask)
dst = cv2.add(img1_bg , img3_fg)
img1[0:rows , 0:cols] = dst

cv2.imshow('res' , img1)
cv2.waitKey(0)
cv2.destroyAllWindows() 