import cv2 as cv
import serial as sp
import time as tm

cam = cv.VideoCapture(0)
cv.namedWindow('Key Logger')
cv.resizeWindow('Key Logger',500,500)
Port = sp.Serial('COM4',9600)
tm.sleep(3)
while(cam.isOpened):
    k = cv.waitKey(5000)
    if(k == 112):
        print('Moving to the Right')
        Port.write('p\r\n')
    if(k == 111):
        print('Moving to the Forward')
        Port.write('o\r\n')
    if(k == 105):
        print('Moving to the Left')
        Port.write('i\r\n')
    if(k == 108):
        print('Moving to the Backwrd')
        Port.write('l\r\n')


