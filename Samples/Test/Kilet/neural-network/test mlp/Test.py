__author__ = 'BENGEOS-PC'
from mlxtend.data import mnist_data
from matplotlib import pyplot as plt
def plot_digit(X,y,idx):
    img = X[idx].reshape(28,28)
    plt.imshow(img,cmap='Greys',interpolation='nearest')
    plt.title('True Lable: %'% y[idx])
    plt.show()
X,y = mnist_data()
plot_digit(X,y,4)