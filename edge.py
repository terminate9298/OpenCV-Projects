import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
	_ , frame = cap.read()
	#laplacian Filter 

	# laplacian = cv2.Laplacian(frame,cv2.CV_64F)
	# sobelx = cv2.Sobel(frame , cv2.CV_64F , 1 , 0 , ksize=5)
	# sobely = cv2.Sobel(frame , cv2.CV_64F , 0 , 1 , ksize=5)
	blur = cv2.GaussianBlur(frame, (15,15) , 0)
	median = cv2.medianBlur(frame , 15)
	edges = cv2.Canny(median , 0 ,200)
	edges2 = cv2.Canny(frame , 0 ,200)
	cv2.imshow('Original', frame)
	cv2.imshow('Edges' , edges)
	cv2.imshow('Edges2' , edges2)
	# cv2.imshow('blur',blur)
	# cv2.imshow('median',median)
	# cv2.imshow('Laplacian', laplacian)
	# cv2.imshow('Sobelx', sobelx)
	# cv2.imshow('Sobely', sobely)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cv2.release()
