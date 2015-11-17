__author__ = 'BENGEOS-PC'
import My_MLP_1 as My_Net
import Network as NT
import mnist_loader as mn
from numpy import *
def vectorized_result(Val,size):
    e = zeros((size, 1))
    e[Val] = 1.0
    return e
net1 = NT.Network([784, 10, 10])
net2 = My_Net.My_MLP([784, 50,10])
training_data, validation_data, test_data = mn.load_data_wrapper()
#net1.SGD(training_data, 1, 10, 3.0,test_data)
#net2.evaluate_network(training_data,10,10,3.0,test_data)
X= []
X.append(array([[1,2,3,4,5]]))
X.append(array([[1,0,2,1,0]]))
X.append(array([[1,2,6,2,9]]))
X.append(array([[8,0,0,0,9]]))
X.append(array([[8,2,4,0,9]]))
Y = []
Y.append(0)
Y.append(1)
Y.append(2)
Y.append(3)
Y.append(4)

training_inputs = [reshape(x, (5, 1)) for x in X]
training_results = [vectorized_result(y,5) for y in Y]
test_result = [reshape(x, (1, 1)) for x in Y]
training_data = zip(training_inputs, training_results)
test_data = zip(training_inputs,test_result)
print 'Print Input'
print training_data




net2 = My_Net.My_MLP([5, 20,5])
net2.evaluate_network(training_data,60,2,3.0,test_data)
print net2.weights


