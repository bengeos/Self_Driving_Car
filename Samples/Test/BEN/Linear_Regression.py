__author__ = 'BENGEOS-PC'
import numpy as np
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
    z = z * z
    z = np.sum(z)
    z = z/2
    z = z/len(Training)
    return  z
def gradientDescent(thetha1,thetha2,X,Y,R,min):
    condition = min + 100
    T0 = thetha1
    T1 = thetha2
    while(min <= condition):
        diff1 = hypothesis(X,T0,T1) - Y
        diff1 = R*np.sum(diff1)/len(X)
        update1 = T0 - diff1

        diff2 = hypothesis(X,T0,T1) - Y
        diff2 = diff2 * X
        diff2 = R*np.sum(diff2)/len(X)
        update2 = T1 - diff2
        condition = update1
        if(condition<update2):
            condition = update2
        T0 = update1
        T1 = update2
    return T0,T1


t0,t1 = gradientDescent(2,3,x,y,1,0.01)
print(gradientDescent(2,3,x,y,1,0.01))
plt.plot(x,y,'ro')
yy = hypothesis(x,t0,t1)
plt.plot(x,yy,'y')
plt.show()
def drawBars3D():
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    for c,z in zip(['r','g','b','y'],[30,20,10,0]):
        xs = np.arange(20)
        ys = np.random.rand(20)
        ax.bar(xs,ys,zs=z,zdir='y',color=c)
    plt.show()


