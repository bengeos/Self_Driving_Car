__author__ = 'BENGEOS-PC'
import Camera_Module as md
import time
import cv2 as cv
import numpy as np
Cam_Mod = md.Camera_Module(0)
Cam_Mod.Start()
time.sleep(3)
while(1):
    img = Cam_Mod.get_NewImage((200,250),0)
    cv.imshow("Camera1",img)
    print(Cam_Mod.get_ImageArray((10,10),0))
    time.sleep(0.05)