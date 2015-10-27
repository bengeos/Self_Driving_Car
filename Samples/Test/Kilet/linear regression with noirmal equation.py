__author__ = 'Kilet'
import numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as alg
x = np.array([800,940,1050,1240,1300,1320,1390,1440,1450,1500,1670,1800,1950,2000,2020])
y = np.array([170,200,220,255,290,320,350,383,400,422,450,500,540,555,570])
a=np.ones((len(x),2))
a[:,1]=x
a = np.mat(a)
b=np.mat(y).T
T=alg.inv(a.T*a)*a.T*b
def hypothesis(x,t1,t2):
    hyp=t1+t2*x
    return hyp
t1=T[0,0]
t2=T[1,0]
X=np.linspace(800,2020,1000)
Y=hypothesis(X,t1,t2)
plt.plot(X,Y,"b")
plt.plot(x,y,"ro")
plt.show()
