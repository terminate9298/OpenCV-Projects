import cv2
import numpy as np 
# import pyautogui as mo
face_cascade = cv2.CascadeClassifier('face.xml')

eye_cascade = cv2.CascadeClassifier('eye.xml')

cap = cv2.VideoCapture(0)

while True: 
	ret , img = cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	# faces = face_cascade.detectMultiScale(gray)
	faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y) , (x+w,y+h) , (255,0,0) , 2)
		roi_gray = gray[y:y+h , x:x+w]
		roi_color = img[y:y+h , x:x+w]
		# mo.moveTo(x,y)
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh),(0,255,0), 1)
	cv2.imshow('img',img)
	# x,y,w,h = faces
	# mo.moveTo(x,y)
	k=cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
