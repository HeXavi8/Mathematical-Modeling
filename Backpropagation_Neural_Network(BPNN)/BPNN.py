from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp

def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	# weights number contains an extra one for input theta0 which is always 1 (according to coursera ml course)
	hidden_layer = [{'weights': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(hidden_layer)
	network.append(output_layer)
	return network

def activate(weights, inputs):
	# a = sum(w * input.T) + bias
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

def transfer(activation):
	# sigmoid or reLu or whatever
	return 1.0/ (1.0 + exp(-activation))

def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs

def transfer_derivative(output):
	# d(sigmoid(z)) = z * (1-z), standard bp algorithm
	return output * (1.0 - output)

def backward_propagate(network, expected):
	# error[i] = W * error[i+1] * sigmoid_derivative
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()

		if i == len(network) - 1:
			# first from output layer, just get the output difference
			# note: our difference is expected - output, some other implementing uses output-expected
			#       which causes the weight update is different (weight = weight +/- ....)
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		else:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i+1]:
					# neuron['delta'] saves errors[i+1] * sigmoid_derivateive
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)

		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

def update_weights(network, row, learning_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			# for hidden layer and output layer
			inputs = [neuron['output'] for neuron in network[i-1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += learning_rate * neuron['delta'] * inputs[j]
			# theta0 is always 1 (explained on coursera ml course)
			neuron['weights'][-1] += learning_rate * neuron['delta']

def train_network(network, training_data, learning_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		sum_error = 0
		for row in training_data:
			outputs = forward_propagate(network, row)
			# this is a trick to set the bi-class flag by using the row[-1] as class index
			# expected[0] = 1: expected to be class 1
			# expected[1] = 1: expected to be class 2
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			sum_error += sum([(expected[i] - outputs[i])**2 for i in range(len(expected))])
			backward_propagate(network, expected)
			update_weights(network, row, learning_rate)
		print('>epoch: %d, learning rate: %.3f, error: %.3f' % (epoch, learning_rate, sum_error))


def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))

seed(1)
dataset = [[2.7810836,2.550537003,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1]]

test_data = [[1.465489372,2.362125076,0],
			[8.675418651,-0.242068655,1],
			[7.673756466,3.508563011,1]]

n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.5, 20, n_outputs)
for layer in network:
	print(layer)

for row in test_data:
	result = predict(network, row)
	print('expected: %d, predicted: %d\n' % (row[-1], result))