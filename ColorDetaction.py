import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read() 					        # Take each frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)	# Convert BGR to HSV
    lower = np.array([0, 120, 70])			        # define range of color in HSV
    upper = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)		
    cv2.imshow('res',res)                           #Only show the colors specified in the range

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
