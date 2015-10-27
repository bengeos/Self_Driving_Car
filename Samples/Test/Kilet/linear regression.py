__author__ = 'Kilet'
import numpy as np
from matplotlib import pyplot as plt
x = np.array([800,940,1050,1240,1300,1320,1390,1440,1450,1500,1670,1800,1950,2000,2020])
y = np.array([170,200,220,255,290,320,350,383,400,422,450,500,540,555,570])
plt.plot(x,y,"bo")
plt.show()
def hypothesis(x,t1,t2):
    hyp=t1+t2*x
    return hyp
def costfun(x,y,t1,t2):
    d= hypothesis(x,t1,t2)-y
    d=d*d
    s=np.sum(d)
    j= s/(2*len(x))
    return j
val=costfun(x,y,0,1)
print(val)
def gradientdecent(x,y,t1,t2,r):
    T1=t1
    T2=t2
    cond= r+1
    while(cond>r):
        c0=2*r*np.sum(hypothesis(x,T1,T2)-y)
        c1=2*r*np.sum((hypothesis(x,T1,T2)-y)*x)
        cond=c0
        if(cond<c1):
            cond=c1
        T1=T1-c0
        T2=T2-c1
    return T1,T2
val1=gradientdecent(x,y,2,3,0.001)
print(val1)
