__author__ = 'Kilet'
import cv2 as cv
import threading
class Camera(threading.Thread):
    def __init__(self,Cam_Num):
        threading.Thread.__init__(self)
        self.Cam_Num = Cam_Num
        self.Cap = cv.VideoCapture(self.Cam_Num)
        self.Image = self.cap_img()
    def cap_img(self):
        state,img = self.Cap.read()
        cv.waitKey(10)
        return img
    def run(self):
        while(self.Cap.isOpened):
            state,self.Image = self.Cap.read()
            print("Thread",self.Image)
    def get_image(self):
        cv.waitKey(10)
        return self.Image
C1 = Camera(0)
C1.start()
print(C1.get_image())
