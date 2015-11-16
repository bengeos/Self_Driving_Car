__author__ = 'BENGEOS-PC'
from numpy import *
import numpy as np
class My_MLP(object):
    def __init__(self,Network_Shape):
        self.num_layers = len(Network_Shape)
        self.Network_Shape = Network_Shape
        self.biases = self.init_biases()
        self.weights = self.init_weight()
    def init_biases(self):
        Biases = [np.random.randn(i,1) for i in self.Network_Shape[1:]]
        return Biases
    def init_weight(self):
        Weights = [np.random.randn(i,j) for j,i in zip(self.Network_Shape[:-1],self.Network_Shape[1:])]
        return Weights
    def forward(self,inputX):
        for b,w in zip(self.bias,self.weights):
            a = sigmoid(np.dot(w,inputX)+b)
        return a
    def backward(self,x,y):
        _bias = [np.zeros(b.shape) for b in self.biases]
        _weight = [np.zeros(w.shape) for w in self.weights]
        act = x
        Acts = [x]
        Vects = []
        for b,w in zip(self.biases,self.weights):
            z = np.dot(w,act)+ b
            Vects.append(z)
            act = sigmoid(z)
            Acts.append(act)
        Delta = self.cost_error(Acts[-1],y) * sigmoid_derv(Vects[-1])
        _bias[-1] = Delta
        _weight[-1] = np.dot(Delta,Acts[-2].transpose())
        for i in xrange(2,self.num_layers):
            v = Vects[-i]
            Derv = sigmoid_derv(v)
            Delta = np.dot(self.weights[-i+1].transpose(),Delta)*Derv
            _bias[-i] = Delta
            _weight[-i] = np.dot(Delta,Acts[-i+1].transpose())
        return  (_bias, _weight)
    def cost_error(self,O_Act,T_Y):
        val = O_Act - T_Y
        return val
    def evaluate_network(self,Training_Data,loop,min_size,rate,Test_Data):
        if Test_Data: n_test = len(Test_Data)
        n = len(Training_Data)
        for j in xrange(loop):
            random.shuffle(Training_Data)
            mini_batches = [
                Training_Data[k:k+min_size]
                for k in xrange(0, n, min_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, rate)
            if Test_Data:
                print "Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(Test_Data), n_test)
            else:
                print "Epoch {0} complete".format(j)
    def update_mini_batch(self, mini_batch, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The ``mini_batch`` is a list of tuples ``(x, y)``, and ``eta``
        is the learning rate."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backward(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
    def update_min_batch(self,min_batch,rate):
        _bias = [np.zeros(b.shape) for b in self.biases]
        _weight = [np.zeros(w.shape) for w in self.weights]
        for x,y in min_batch:
            delta_b,delta_w = self.backward(x,y)
            _bias = [nb+dnb for nb, dnb in zip(_bias, delta_b)]
            _weight = [nw+dnw for nw, dnw in zip(_weight, delta_w)]
        self.weights = [w-(rate/len(min_batch))*nw for w, nw in zip(self.weights, _weight)]
        self.biases = [b-(rate/len(min_batch))*nb for b, nb in zip(self.biases, _bias)]
    def evaluate(self, test_data):
        test_results = [(np.argmax(self.forward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
def sigmoid(inputX):
    val = 1.0/(1.0 + np.exp(-inputX))
    return val
def sigmoid_derv(inputX):
    val = sigmoid(inputX)*(1-sigmoid(inputX))
    return val