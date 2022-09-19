#Detect Blue

import cv2;
import numpy as np
cam=cv2.VideoCapture(0);

while (1):
    ret, frame = cam.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBlue= np.array([110,50,50])
    upperBlue= np.array([130,255,255])
    mask= cv2.inRange(hsv, lowerBlue, upperBlue)
    res= cv2.bitwise_and(ret,frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    #k= cv2.waitKey(5) & 0xFF
    #if k==27:
    #    break
    #cv2.destroyAllWindows()
    #cam.release()
    
    if cv2.waitKey(10) == ord("q"):
        break
    