import cv2 
import numpy as np 
cap = cv2.VideoCapture('tracking2.avi') 
while(1): # Take each frame 
    _, frame = cap.read() 
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    # define range of blue color in HSV
    lower_blue = np.array([10,128,128]) 
    upper_blue = np.array([60,255,255]) 
    # Threshold the HSV image to get only blue colors 
    mask = cv2.inRange(hsv, lower_blue, upper_blue) #lower 과 upper 사이에 있으면 흰색 나머지는 검은색
    # Bitwise-AND mask and original image 
    res = cv2.bitwise_and(frame,frame, mask= mask) #오리지널 컬러값만 가져옴
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) 
    k = cv2.waitKey(5) & 0xFF 
    if k == 27: 
        break 
cv2.destroyAllWindows()