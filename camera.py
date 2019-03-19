import cv2
import numpy as np 
#0,1,2 depend on camera of computer 
cap = cv2.VideoCapture(0)
#for saving the video to local file you have to use codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#for saving the video to computer
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True: 
	ret, frame = cap.read()
	#for converting it to gray scale vedio 
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#for saving the file
	out.write(frame)
	#for shwoing the file
	cv2.imshow('frame',frame)
	cv2.imshow('gray',gray)
	#for exiting the window
	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break
cap.release()
out.release()
cv2.destroyAllWindows()