__author__ = 'Shanti'
import numpy as np
from matplotlib import pyplot as pnt

x = np.array([800,940,1050,1240,1300,1320,1390,1440,1450,1500,1670,1800,1950,2000,2020])
y = np.array([170,200,220,255,290,320,350,383,400,422,450,500,540,555,570])
pnt.plot (x,y,"ro")
pnt.show()