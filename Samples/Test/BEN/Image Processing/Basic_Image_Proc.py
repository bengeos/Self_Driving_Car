import cv2 as cv
import numpy as np

Network_Shape = [500,50,20,10,5,3,5]
weights = [np.random.randn(i,j) for j,i in zip(Network_Shape[:-1],Network_Shape[1:])]
print(weights[0])
def Create_Image(NetShape,Weight,HSpacing,VSpacing):
    Width = int((len(NetShape)+1)*HSpacing)
    Height = int((max(NetShape)+1)*VSpacing)
    pic = np.zeros((Width,Height,3), np.uint8)
    X_pnt = HSpacing
    Layer = 0
    for loc in NetShape:
        Y_pnt = (Height - (loc-1)*VSpacing)/2
        for aa in range(loc):
            cv.circle(pic,(Y_pnt,X_pnt),10,(255,0,0),2)
            if(Layer>0):
                bb = (Height - (NetShape[Layer-1]-1)*VSpacing)/2
                print('------>',NetShape[Layer-1])
                for w in range(np.shape(weights[Layer-1])[1]):
                    cv.line(pic,(bb,X_pnt-HSpacing),(Y_pnt,X_pnt),(0,255,0),1)
                    bb = bb+VSpacing
            Y_pnt = Y_pnt+VSpacing
        X_pnt = X_pnt + HSpacing
        Layer = Layer + 1;
    return pic
weights = [np.random.randn(i,j) for j,i in zip(Network_Shape[:-1],Network_Shape[1:])]
cam = cv.VideoCapture(0)
img = Create_Image(Network_Shape,weights,200,40)
cv.imwrite('Ben.png',img)
while(cam.isOpened):
    cv.imshow('JMKjskdasd',img)
    cv.waitKey(10)


print(weights)
print('____________________________')
print(weights[:-1])
print(max(Network_Shape))

