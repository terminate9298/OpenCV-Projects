import cv2
import numpy as np 

img_brg = cv2.imread('search.jpg')
img_gray = cv2.cvtColor(img_brg , cv2.COLOR_BGR2GRAY)

template = cv2.imread('match.jpg',0)
w , h = template.shape[::-1]

res = cv2.matchTemplate(img_gray , template , cv2.TM_CCOEFF_NORMED)

threshold = 0.70
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_brg , pt , (pt[0]+w , pt[1]+h), (0 , 255 , 255) , 2 )

cv2.imshow('detected',img_brg)	
cv2.waitKey(0)
cv2.destroyAllWindows() 