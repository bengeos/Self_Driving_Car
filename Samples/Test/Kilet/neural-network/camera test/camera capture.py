__author__ = 'Kilet'
import cv2 as cv
cap = cv.VideoCapture(0)
while(cap.isOpened):
    stat,img = cap.read()
   # cv.imshow("camera", img)
    cv.imshow("Camera",img)
    cv.waitKey(15)
cv.destroyAllWindows()
cap.release()
