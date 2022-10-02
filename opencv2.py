import cv2
import numpy as np

path = "D:\\CUP\\bahe\\RawVideo\\Positive\\P_002.mp4"

face_xml = cv2.CascadeClassifier('./xml/cascade.xml')
img = cv2.VideoCapture(path)
# img = cv2.imread('4.png')

print("Video path\n",path)


while img.isOpened():
    ret, frame = img.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_xml.detectMultiScale(gray,1.5, 3, 0,(10,10),(80,80))
    print('face=',len(faces))
    # draw
    if(len(faces) <= 10):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
   
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(30) & 0xFF == 27 :
        break 