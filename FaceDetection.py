import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.flip(frame,1)
    gry = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # f=cv.CascadeClassifier(r"C:\Users\shoai\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_eye.xml")
    f=cv.CascadeClassifier(r"C:\Users\shoai\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
    d = f.detectMultiScale(gry,2,1)
    for(x,y,w,h) in d:

        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),-1)
    
    cv.imshow('frame',frame)
    if cv.waitKey(1)==ord('q') or ret ==False:
        break
cap.release()
cv.destroyAllWindows()