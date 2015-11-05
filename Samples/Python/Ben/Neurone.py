__author__ = 'BENGEOS-'
import numpy as np
from matplotlib import pyplot as plt

x1 = np.mat(np.array([0,1,0,1]))
x2 = np.mat(np.array([0,0,1,1]))

y = np.mat(np.array([0,0,0,1]))

def sigmoid(X):
    return (1./(1+np.exp(-X)))
def mul_ele(X1,X2):
    R = []
    for i in range(np.shape(X1)[0]):
        r = []
        for j in range(np.shape(X1)[1]):
            r.append(X1[i,j]*X2[i,j])
        R.append(r)
    return np.mat(R)
def Forward(param,X):
    return X
x1 = np.mat(np.array([1,2,3]))
x2 = np.mat(np.array([1,2,5]))

x1 = np.array([3,5,8,9])
print(x1[-2])