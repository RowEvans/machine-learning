import numpy as np

# X is the dataset common term for what it is being trained on
X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons) # n_inputs: shape of the input coming in (single sample), n_neurons: how many neurons do you created?
        self.biases = np.zeros((1, n_neurons)) # returns a matrix based on the size of the tuple given

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)