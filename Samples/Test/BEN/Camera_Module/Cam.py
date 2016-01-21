import cv2 as cv
cam = cv.VideoCapture(0)
while(cam.isOpened):
    st,img = cam.read()
    cv.imshow('Camera',img)
    cv.waitKey(10)