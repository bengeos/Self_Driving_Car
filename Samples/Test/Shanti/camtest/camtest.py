__author__ = 'Shantii'
import cv2 as cv
import math
cap= cv.VideoCapture(0)
while (cap.isOpened):
    stat,img = cap.read()
    cv.imshow("camera",img)
    cv.waitKey(10)
cv.destroyAllWindows()
cap.release()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imgshow('frame',gray)
