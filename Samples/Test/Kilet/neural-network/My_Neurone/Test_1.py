__author__ = 'BENGEOS-PC'
import cv2
import My_MLP_1 as My_Net
import Network as NT

import mnist_loader as mn
from numpy import *
import numpy as np

def vectorized_result(Val,size):
    e = zeros((size, 1))
    e[Val] = 1.0
    return e

img = cv2.imread('Data/digits.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cells = [hsplit(row,100) for row in vsplit(img_gray,50)]
imgs = array(cells)
XX = []
YY = []
num = 0
for i in range(50):
    num = int(i/5)
    for j in xrange(0,5):
        train_data = imgs[i,j].reshape(-1,400).astype(float32)
        train_resu = num
        XX.append(train_data)
        YY.append(train_resu)
XX1 = []
YY1 = []
num = 0
for i in xrange(50):
    num = int(i/5)
    for j in xrange(99,100):
        train_data = imgs[i,j].reshape(-1,400).astype(float32)
        train_resu = num
        XX1.append(train_data)
        YY1.append(train_resu)


training_inputs = [reshape(x, (400, 1)) for x in XX]
training_results = [vectorized_result(y,10) for y in YY]
test_inputs = [reshape(x, (400, 1)) for x in XX]
test_result = [reshape(x, (1, 1)) for x in YY]
training_data = zip(training_inputs, training_results)
test_data = zip(test_inputs,test_result)

net2 = My_Net.My_MLP([400,300,150,50,10])
net2.evaluate_network(training_data,1000,10,3.0,test_data)