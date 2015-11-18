__author__ = 'BENGEOS-PC'
import Camera as cm
import time
import cv2 as cv


C1 = cm.Camera(0)
C1.start()
time.sleep(5)
x = 10
cond = True
while(cond):
    x = x - 1
    time.sleep(0.5)
    print(C1.get_image())
    cv.imshow("Thread Image",C1.get_image())
    print('>>>>>>>>>>>',x)
    if(x == 0):
        C1.Stop()
