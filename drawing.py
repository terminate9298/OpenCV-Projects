import numpy as np 
import cv2

#reading the file
img = cv2.imread('bit.jpg' , cv2.IMREAD_COLOR)

#Drawing on the file , from , to , color , width
cv2.line(img , (0,0) , (150,150) , (255,255,255) , 15)
#Drawing the rectangle on the file , from , to , color , width
cv2.rectangle(img , (15,25) , (100,100) , (0,255,0) , 5)
#Drawing the circle on the file ,center ,radius , color , width
#negative width will fill the shape
cv2.circle(img , (100,50) , 20 ,(100,100,100) , -1)

#make the array of points to put on the image
pts = np.array([[10,2],[30,34],[12,23],[54,43],[23,65]], np.int32)
#pts = pts.reshape((-1,1,2))
#drawing the polygons on imagewith points , connecting the first and last point , color and width
cv2.polylines(img, [pts] , True , (0,255,255) , 5) 
#using the font 

#THE FONT TO USE
font = cv2.FONT_HERSHEY_SIMPLEX
#text to put on , text , (startingplace) , FONT ,SIZE ,COLOR , DISTANCE BETWEEN THE WORDS AND THE ALIGNMENT OF WORDS IN ROW

cv2.putText(img, 'Open CV Rocks!!',(0,123),font,1, (200,200,200) , 1 ,cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()