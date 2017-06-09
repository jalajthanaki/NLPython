#The credits for this code go to Ludo Bouan.
# I've merely created a wrapper to get people started.

import numpy as np
np.seterr(over='ignore')

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)  # Seed the random number generator
        self.weights = {}  # Create dict to hold weights
        self.num_layers = 1  # Set initial number of layer to one (input layer)
        self.adjustments = {}  # Create dict to hold adjustements

    def add_layer(self, shape):
        # Create weights with shape specified + biases
        self.weights[self.num_layers] = np.vstack((2 * np.random.random(shape) - 1, 2 * np.random.random((1, shape[1])) - 1))
        # Initialize the adjustements for these weights to zero
        self.adjustments[self.num_layers] = np.zeros(shape)
        self.num_layers += 1

    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def predict(self, data):
        # Pass data through pretrained network
        for layer in range(1, self.num_layers+1):
            data = np.dot(data, self.weights[layer-1][:, :-1]) + self.weights[layer-1][:, -1] # + self.biases[layer]
            data = self.__sigmoid(data)
        return data

    def __forward_propagate(self, data):
        # Progapagate through network and hold values for use in back-propagation
        activation_values = {}
        activation_values[1] = data
        for layer in range(2, self.num_layers+1):
            data = np.dot(data.T, self.weights[layer-1][:-1, :]) + self.weights[layer-1][-1, :].T # + self.biases[layer]
            data = self.__sigmoid(data).T
            activation_values[layer] = data
        return activation_values

    def simple_error(self, outputs, targets):
        return targets - outputs

    def sum_squared_error(self, outputs, targets):
        return 0.5 * np.mean(np.sum(np.power(outputs - targets, 2), axis=1))

    def __back_propagate(self, output, target):
        deltas = {}
        # Delta of output Layer
        deltas[self.num_layers] = output[self.num_layers] - target

        # Delta of hidden Layers
        for layer in reversed(range(2, self.num_layers)):  # All layers except input/output
            a_val = output[layer]
            weights = self.weights[layer][:-1, :]
            prev_deltas = deltas[layer+1]
            deltas[layer] = np.multiply(np.dot(weights, prev_deltas), self.__sigmoid_derivative(a_val))

        # Caclculate total adjustements based on deltas
        for layer in range(1, self.num_layers):
            self.adjustments[layer] += np.dot(deltas[layer+1], output[layer].T).T

    def __gradient_descente(self, batch_size, learning_rate):
        # Calculate partial derivative and take a step in that direction
        for layer in range(1, self.num_layers):
            partial_d = (1/batch_size) * self.adjustments[layer]
            self.weights[layer][:-1, :] += learning_rate * -partial_d
            self.weights[layer][-1, :] += learning_rate*1e-3 * -partial_d[-1, :]


    def train(self, inputs, targets, num_epochs, learning_rate=1, stop_accuracy=1e-5):
        error = []
        for iteration in range(num_epochs):
            for i in range(len(inputs)):
                x = inputs[i]
                y = targets[i]
                # Pass the training set through our neural network
                output = self.__forward_propagate(x)

                # Calculate the error
                loss = self.sum_squared_error(output[self.num_layers], y)
                error.append(loss)

                # Calculate Adjustements
                self.__back_propagate(output, y)

            self.__gradient_descente(i, learning_rate)

            # Check if accuarcy criterion is satisfied
            if np.mean(error[-(i+1):]) < stop_accuracy and iteration > 0:
                break

        return(np.asarray(error), iteration+1)



if __name__ == "__main__":

    # ----------- XOR Function -----------------

    # Create instance of a neural network
    nn = NeuralNetwork()

    # Add Layers (Input layer is created by default)
    nn.add_layer((2, 9))
    nn.add_layer((9, 1))

    # XOR function
    training_data = np.asarray([[0, 0], [0, 1], [1, 0], [1, 1]]).reshape(4, 2, 1)
    training_labels = np.asarray([[0], [1], [1], [0]])

    error, iteration = nn.train(training_data, training_labels, 5000)
    print('Error = ', np.mean(error[-4:]))
    print('Epoches needed to train = ', iteration)

    # nn.predict(testing_data)