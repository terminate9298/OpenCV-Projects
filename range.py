import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	_ , frame = cap.read()
#underscore is used as it will neglect the returning value 
#its easier to waork with hsv so converting to hsv
	hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
#array of range of color
	lower_red = np.array([0,175,20])
	upper_red = np.array([200,255,150])
#creating the mask for inrange colors
	mask = cv2.inRange(hsv , lower_red , upper_red)
	res = cv2.bitwise_and(frame , frame ,mask = mask)
	#for bluring the mask
	# kernel = np.ones((15 , 15) , np.float32)/225
	# smoothed = cv2.filter2D(res , -1 , kernel)
#differnet types of blur in cv2
	# blur = cv2.GaussianBlur(res, (15,15) , 0)
	# median = cv2.medianBlur(res , 15)
	# bilateral = cv2.bilateralFilter( res, 15 , 75 , 75 )
	
#for clearing the vedio use various important filters

	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask , kernel , iterations = 1)
	dilation = cv2.dilate(mask , kernel ,iterations = 1)
	opening = cv2.morphologyEx(mask , cv2.MORPH_OPEN , kernel)
	closing = cv2.morphologyEx(mask , cv2.MORPH_CLOSE , kernel)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('erosion',erosion)
	cv2.imshow('dilation',dilation)
	cv2.imshow('opening',opening)
	cv2.imshow('closing',closing)
	#cv2.imshow('Smoothed' , smoothed)
	# cv2.imshow('Gaussian' , blur)
	# cv2.imshow('Median ', median)
	# cv2.imshow('Bilateral ' ,bilateral)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cv2.release()
