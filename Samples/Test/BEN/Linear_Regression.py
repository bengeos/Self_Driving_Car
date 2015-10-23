__author__ = 'BENGEOS-PC'
import numpy as np
from numpy import linalg as alg
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.array([800,940,1050,1240,1300,1320,1390,1440,1450,1500,1670,1800,1950,2000,2020])
y = np.array([170,200,220,255,290,320,350,383,400,422,450,500,540,555,570])

def plotPoints(X,Y):
    plt.figure(1)
    plt.plot(X,Y,X,'bo')
    plt.show()

def hypothesis(x,theta1,theta2):
    return theta1 + theta2*x

def costFunc(theta1,theta2,Training,output):
    z = hypothesis(Training,theta1,theta2) - output
    z = np.sum(z * z)/(2*len(Training))
    return z

def gradientDescent(thetha1,thetha2,X,Y,R,min):
    T0 = thetha1
    T1 = thetha2
    for i in range(10):
        cost = costFunc(T0,T1,X,Y)
        t0 = T0 - R*sum((hypothesis(X,T0,T1)-Y))
        t1 = T1 - R*sum((hypothesis(X,T0,T1)-Y)*X)
        T0 = t0
        T1 = t1
        #optimization is needed
        print(T0,T1,cost)
    return T0,T1

print(costFunc(0,1,x,y))

def drawBars3D():
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    for c,z in zip(['r','g','b','y'],[30,20,10,0]):
        xs = np.arange(20)
        ys = np.random.rand(20)
        ax.bar(xs,ys,zs=z,zdir='y',color=c)
    plt.show()


