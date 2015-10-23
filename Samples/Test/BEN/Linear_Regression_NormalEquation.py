__author__ = 'BENGEOS-PC'
import numpy as np
from numpy import linalg as alg
from matplotlib import pyplot as plt

x = np.array([800,940,1050,1240,1300,1320,1390,1440,1450,1500,1670,1800,1950,2000,2020])
y = np.array([170,200,220,255,290,320,350,383,400,422,490,500,540,555,570])
xx = np.array([[3,4],[5,6]])

#initialize the input
def init_Traning(Input):
    val = np.ones((len(Input),1))
    val = np.concatenate((val,np.mat(Input).T),1)
    return val
def Hyp(T0,T1,X):
    return T0 + X*T1
X = init_Traning(x)
Y = np.mat(y).T
val = alg.inv(X.T*X)*X.T*Y

T = np.linspace(600,2020,100)
R = Hyp(val[0,0],val[1,0],T)
plt.plot(x,y,'ro')
plt.plot(T,R,'b')
plt.show()
print(val)