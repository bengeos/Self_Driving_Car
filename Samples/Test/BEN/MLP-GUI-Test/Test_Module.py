import Camera_Module
import time
import cv2 as cv
import MLP as My_Net
import serial as sp
import time as tm
import numpy as np


#Initialize the Neural Network
net2 = My_Net.MLP([2500,100,50,10])
#initilize Data Storages
training_inputs = []
training_result = []

img_shp = 0
cam = Camera_Module.Camera_Module(0)
cam.Start()
time.sleep(3)

def vectorized_result(Val,size):
    e = np.zeros((size, 1))
    e[Val] = 1.0
    return e

def Reset_All():
    for xx in range(len(training_inputs)):
        training_inputs.pop()
    for xx in range(len(training_result)):
        training_result.pop()
    print("Data Reset")
def append_Trianing(img,val):
    img_shp = np.shape(img)
    print(img_shp)
    _data_ = img.reshape(-1,img_shp[0]*img_shp[1]).astype(np.float32)
    training_inputs.append(_data_)
    training_result.append(val)
    #print np.shape(_data_)
def evaluate_this(img):
    t1 = tm.clock();
    img_shp = np.shape(img)
    _data_ = img.reshape(-1,img_shp[0]*img_shp[1]).astype(np.float32)
    vv = []
    ww = []
    ww.append(2)
    vv.append(_data_)

    test_inputs = [np.reshape(x, (img_shp[0]*img_shp[1], 1)) for x in vv]
    test_result = [np.reshape(x, (1, 1)) for x in ww]
    test_data = zip(test_inputs,test_result)
    res = net2.Evaluate_Data(test_data)
    print('*********************')
    print(res[0])
    if(res[0] == 1):
        print('Moving to the LEFT')
        Port.write('i\r\n')
    if(res[0] == 2):
        print('Moving to the FORWARD')
        Port.write('o\r\n')
    if(res[0] == 3):
        print('Moving to the RIGHT')
        Port.write('p\r\n')
    if(res[0] == 4):
        print('Moving to the BACKWARD')
        Port.write('l\r\n')
    t2 = tm.clock()
    print('Time: ', t2 - t1)
    print '***********************'
def Train_MLP():
    print training_result
    training_inputs1 = [np.reshape(x, (net2.Network_Shape[0], 1)) for x in training_inputs]
    training_result1 = [vectorized_result(y,10) for y in training_result]

    test_inputs = [np.reshape(x, (net2.Network_Shape[0], 1)) for x in training_inputs]
    test_result = [np.reshape(x, (1, 1)) for x in training_result]

    training_data = zip(training_inputs1, training_result1)
    test_data = zip(test_inputs,test_result)

    net2.Evaluate_Network(training_data,10,1,2.0,test_data)





cv.namedWindow('Key Logger')
cv.resizeWindow('Key Logger',500,500)
Port = sp.Serial('COM1',9600)
tm.sleep(3)
auto = 0
while(1):
    #img = cam.get_NewImage((50,50),0)
    img = cv.imread('ben.jpg')
    img_ = img.copy()
    cv.imshow("BEN",cv.resize(img_,(700,500)))
    k = cv.waitKey(100)
    #when "P" pressed
    if(k == 112):
        print('Moving to the Right')
        Port.write('p\r\n')
        print('Append Data: ', len(training_inputs)+1)
        append_Trianing(img,3)
    #when "O" Pressed
    if(k == 111):
        print('Moving to the Forward')
        Port.write('o\r\n')
        print('Append Data: ', len(training_inputs)+1)
        append_Trianing(img,2)
    #When "I" Pressed
    if(k == 105):
        print('Moving to the Left')
        Port.write('i\r\n')
        print('Append Data: ', len(training_inputs)+1)
        append_Trianing(img,1)
    #When "L" Pressed
    if(k == 108):
        print('Moving to the Backwrd')
        Port.write('l\r\n')
        print('Append Data: ', len(training_inputs)+1)
        append_Trianing(img,4)
    #When "T" Pressed
    if(k == 116):
        print '***********************'
        print 'MLP Start to Learn ...'
        print '***********************'
        Train_MLP()
        print 'MLP Finished Lerning!'
        print '***********************'
    #When "R" Pressed
    if(k == 114):
        print '***********************'
        Reset_All()
        print '***********************'
    #When "A" Pressed
    if(k == 97):
        if(auto == 0):
            auto = 1
        else:
            auto = 0
    #When "C" Pressed
    if(k == 99):
        print '***********************'
        print 'Evaluating Current Image ...'
        print '***********************'
        evaluate_this(img)
    #When "S" Pressed
    if(k == 115):
        print '***********************'
        print 'Saving MLP Weights'
        print '***********************'
        net2.Save()
    #When "D" Pressed
    if(k == 100):
        print '***********************'
        print 'Loading XMl Data'
        print '***********************'
        net2.ReadXML()
    #When "E" pressed
    if(k == 101):
        net2.Reset_Weights()
        print '***********************'
        print 'Restarting MLP ...'
        print 'MLP Started'
        print '***********************'
    if(k == 27):
        break
    if(k != -1):
        print(k)
    if(auto == 1):
        evaluate_this(img)