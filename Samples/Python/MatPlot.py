__author__ = 'BENGEOS-PC'
from matplotlib import pyplot as plt
import numpy as np

def drawSine():
    x = np.arange(-10,10,0.2)
    plt.plot(x,np.sin(x),'r--')
    plt.show()
drawSine()
