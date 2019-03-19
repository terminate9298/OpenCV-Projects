import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bit.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR->1  IMREAD_UNCHANGED-> -1 IMREAD_GRAYSCALE->0

#Showing the image with cv2
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img,cmap="gray",interpolation="bicubic")
plt.show()