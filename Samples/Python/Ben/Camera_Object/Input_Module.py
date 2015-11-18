__author__ = 'BENGEOS-PC'
import Camera as cam
class Camera_Module(object):
    def __init__(self,Cam_Num):
        self.Cam_Num = Cam_Num
        self.Camera = cam.Camera(Cam_Num)
