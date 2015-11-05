__author__ = 'BENGEOS-PC'
import numpy as np
from matplotlib import pyplot as plt

x1 = np.array([2,3,8,3,1,9,14,17,12,19,20,11])
x2 = np.array([6,7,2,8,1,3,20,23,19,14,12,18])



def sigmoid(input):
    return (1/(1+np.exp(-input)))
def Forward(param,input):
    return sigmoid(param*input)

A1 = np.mat(np.array([2,3,4]))
A2 = np.mat(np.array([1,2,1]))
print(np.dot(A1,A2))