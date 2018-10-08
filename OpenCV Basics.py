import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)    # This is imgshow
    cv2.imshow('frame1', frame)   # We can have as many frames we like
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):   
        break

'''The above line will allow us to close the camera window & the camera may 
   not show anything without it.
The  'q' in the code will allow us to quit the camera window when we hit q'''
