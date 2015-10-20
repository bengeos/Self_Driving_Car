__author__ = 'BENGEOS-PC'
from matplotlib import pyplot as plt
import numpy as np

def drawSine():
    x = np.arange(-10,10,0.2)
    plt.plot(x,np.sin(x),'r--')
    plt.show()

def drawPoints():
    x = [2,4,5.6,7,10]
    y = [2,10,20,2,6]
    plt.plot(x,y,'ro')
    plt.show()


drawPoints()
plt.plot(np.random.normal(5,4,100),np.random.normal(10,7,100),'ro')
plt.show()