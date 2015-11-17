__author__ = 'BENGEOS-PC'
__author__ = 'BENGEOS-PC'
from numpy import *
import numpy as np
from matplotlib import pyplot as plt
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
    def sigmoid(self,inputX):
        val = 1.0/(1.0 + np.exp(-inputX))
        return val
    def sigmoid_derv(self,inputX):
        val = self.sigmoid(inputX)*(1-self.sigmoid(inputX))
        return val
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
    def forward(self,inputX):
        for b,w in zip(self.biases,self.weights):
            a = sigmoid(np.dot(w,inputX)+b)
        return a
    def evaluate_network(self, Training_Data, loop, min_size, eta,Test_Data=None):
        if Test_Data: n_test = len(Test_Data)
        n = len(Training_Data)
        x = []
        y = []
        for j in xrange(loop):
            random.shuffle(Training_Data)
            mini_batches = [Training_Data[k:k+min_size]for k in xrange(0, n, min_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if Test_Data:
                val = self.evaluate(Test_Data)
                x.append(j)
                y.append(float(val)/n_test*100)
                print "Loop {0}: {1} / {2} | {3}%".format(j,val , n_test,float(val)/n_test*100)
            else:
                print "Loop {0} complete".format(j)
        if Test_Data:
            plt.plot(x,y)
            plt.show()

    def update_mini_batch(self, mini_batch, eta):
        _bias = [np.zeros(b.shape) for b in self.biases]
        _weight = [np.zeros(w.shape) for w in self.weights]
        for x,y in mini_batch:
            delta_b,delta_w = self.backprop(x,y)
            _bias = [nb+dnb for nb, dnb in zip(_bias, delta_b)]
            _weight = [nw+dnw for nw, dnw in zip(_weight, delta_w)]
        self.weights = [w-(eta/len(mini_batch))*nw for w, nw in zip(self.weights, _weight)]
        self.biases = [b-(eta/len(mini_batch))*nb for b, nb in zip(self.biases, _bias)]

    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        for l in xrange(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y)for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        return (output_activations-y)

def sigmoid(z):

    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))