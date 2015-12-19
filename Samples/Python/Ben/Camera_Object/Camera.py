__author__ = 'BENGEOS-PC'
import cv2 as cv
import threading
class Camera(threading.Thread):
    def __init__(self,Cam_Num):
        threading.Thread.__init__(self)
        self.Cam_Num = Cam_Num
        self.Cap = cv.VideoCapture(self.Cam_Num)
        self.Image = self.cap_img()
        self.isRunning = True
    def cap_img(self):
        state,img = self.Cap.read()
        cv.waitKey(10)
        return img
    def run(self):
        while(self.Cap.isOpened and self.isRunning):
            state,self.Image = self.Cap.read()
            #print("Threading .....")
    def get_image(self):
        cv.waitKey(10)
        return self.Image
    def Stop(self):
        self.isRunning = False

