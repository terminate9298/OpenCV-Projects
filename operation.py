import numpy as np 
import cv2

img  = cv2.imread('bit.jpg',cv2.IMREAD_COLOR)
px = img[12,23]
print(px)

img[100:150 , 100:150] = [255,255,255]
face = img[37:111 , 107:194]
img[0:74 , 0:87] = face
 
cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()