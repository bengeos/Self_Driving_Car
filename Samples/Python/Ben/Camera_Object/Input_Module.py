__author__ = 'BENGEOS-PC'
import Camera as cam
import cv2 as cv
import numpy as np

class Camera_Module(object):
    def __init__(self,Cam_Num):
        self.Cam_Num = Cam_Num
        self.Camera = cam.Camera(Cam_Num)
    def Start(self):
        self.Camera.start()
    def Stop(self):
        self.Camera.Stop()
    def get_CVT(self,Color_CHG):
        return cv.cvtColor(self.Camera.get_image(),Color_CHG)
    def get_NewImage(self,New_Size,Image_Type):
        img = self.Camera.get_image()
        img1 = cv.cvtColor(img,self.get_Channle(Image_Type))
        img2 = cv.resize(img1,New_Size)
        return img2
    def get_Channle(self,type):
        New_CHN = cv.COLOR_BGR2GRAY
        if(type == 0):
            New_CHN = cv.COLOR_BGR2GRAY
        elif(type == 1):
            New_CHN = cv.COLOR_BGR2HLS
        elif(type == 2):
            New_CHN = cv.COLOR_BGR2RGB
        return New_CHN
    def get_ImageArray(self,Image_Size,Image_Type):
        img = self.get_NewImage(Image_Size,Image_Type)
        shp = np.shape(img)
        img_array = img.reshape(-1,shp[0]*shp[1])
        return img_array