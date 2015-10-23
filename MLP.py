__author__ = 'BENGEOS-PC'
import numpy as np
from matplotlib import pyplot as plt
def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))
def sigmoid_der(z):
    return sigmoid(z)*(1-sigmoid(z))
class MLP(object):
    def __init__(self,Network_Shape):
        self.Layer_Len = len(Network_Shape)
        self.Network_Shape = Network_Shape
        self.Biases = self.init_Biases()
        self.Weights = self.init_Weight()
    def init_Biases(self):
        biases = [np.random.randn(i,1) for i in self.Network_Shape[1:]]
        return biases
    def init_Weight(self):
        weights = [np.random.randn(i,j) for j,i in zip(self.Network_Shape[:-1],self.Network_Shape[1:])]
        return weights
    def Forward(self,X_Input):
        for b, w in zip(self.Biases, self.Weights):
            X_Input = sigmoid(np.dot(w, X_Input)+b)
        return X_Input
    def Backward(self,x_Input,y_Output):
        _biases = [np.zeros(b.shape) for b in self.Biases]
        _weights = [np.zeros(w.shape) for w in self.Weights]
        activation = x_Input
        activations = [x_Input]
        zs = []
        #Forward Propagation---and store activations in every line
        for b, w in zip(self.Biases, self.Weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        #Get Delta for the output layer from the activation
        delta = self.Cost_Derivative(activations[-1], y_Output) * sigmoid_der(zs[-1])
        _biases[-1] = delta
        _weights[-1] = np.dot(delta, activations[-2].transpose())
        #back propagate the output Delta to the inner layers
        for l in xrange(2, self.Layer_Len):
            z = zs[-l]
            sp = sigmoid_der(z)
            delta = np.dot(self.Weights[-l+1].transpose(), delta) * sp
            _biases[-l] = delta
            _weights[-l] = np.dot(delta, activations[-l-1].transpose())
        return (_biases, _weights)
    def Cost_Derivative(self, output_activations, y):
        return (output_activations-y)
    def Mini_Batch(self, mini_batch, eta):
        _bias = [np.zeros(b.shape) for b in self.Biases]
        _weight = [np.zeros(w.shape) for w in self.Weights]
        for x_val,y_val in mini_batch:
            delta_b,delta_w = self.Backward(x_val,y_val)
            _bias = [nb+dnb for nb, dnb in zip(_bias, delta_b)]
            _weight = [nw+dnw for nw, dnw in zip(_weight, delta_w)]
        self.Weights = [w-(eta/len(mini_batch))*nw for w, nw in zip(self.Weights, _weight)]
        self.Biases = [b-(eta/len(mini_batch))*nb for b, nb in zip(self.Biases, _bias)]
    def Evaluate_Network(self, Training_Data, loop, min_gap, eta,Test_Data=None):
        if Test_Data: n_test = len(Test_Data)
        n = len(Training_Data)
        x = []
        y = []
        for j in xrange(loop):
            np.random.shuffle(Training_Data)
            mini_batches = [Training_Data[k:k+min_gap]for k in xrange(0, n, min_gap)]
            for mini_batch in mini_batches:
                self.Mini_Batch(mini_batch, eta)
            if Test_Data:
                val = self.Evaluate(Test_Data)
                x.append(j)
                y.append(float(val)/n_test*100)
                print "Loop {0}: {1} / {2} | {3}%".format(j,val , n_test,float(val)/n_test*100)
            else:
                print "Loop {0} complete".format(j)
        if Test_Data:
            plt.plot(x,y)
            plt.show()
    def Evaluate(self, test_data):
        test_results = [(np.argmax(self.Forward(x)), y)for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)
    def get_LineArray(self,Mat_x):
        lines = []
        for i in range(np.shape(Mat_x)[0]):
            line = ''
            for j in range(np.shape(Mat_x)[1]):
                if(j == 0):
                    line = str(Mat_x[i,j])
                else:
                    line = line + ' '+ str(Mat_x[i,j])
            lines.append(line)
        return lines
    def Weights_to_Array(self):
        Param_Lines = []
        for i in range(self.Layer_Len - 1):
            _weights = self.Weights[i]
            lines = self.get_LineArray(_weights)
            for line in lines:
                Param_Lines.append(line)
            Param_Lines.append('*********************************')
        return Param_Lines
#kilet added this

