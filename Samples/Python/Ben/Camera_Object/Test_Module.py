__author__ = 'BENGEOS-PC'
import Input_Module as md
import time
import cv2 as cv
Cam_Mod = md.Camera_Module(0)
Cam_Mod.Start()
time.sleep(3)
while(1):
    cv.imshow("Camera1",Cam_Mod.get_NewImage((700,500),2))
    time.sleep(0.01)