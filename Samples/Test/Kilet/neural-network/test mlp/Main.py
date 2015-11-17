__author__ = 'BENGEOS-PC'
from  numpy import *
import cv2
cam = cv2.VideoCapture(0)
while(cam.isOpened):
    state,img = cam.read()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_edge = cv2.Canny(img_gray,100,100)
    print shape(img_gray)
    cv2.imshow('Camera',img_gray)
    cv2.waitKey(10)
cam.release()
cv2.destroyAllWindows()