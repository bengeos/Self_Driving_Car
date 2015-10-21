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
def damped(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, damped(t1), 'bo', t2, damped(t2), 'k')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()