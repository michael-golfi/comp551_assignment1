import numpy as np
import pandas as pd
import csv
import math
from decimal import *
import matplotlib.pyplot as plt
import random

def getData(csv_file):
	formatted_matrix = []
	extracted_data = []
	with open(csv_file,'rb') as csvfile:
		reader = csv.reader(csvfile)
		for record in reader:
			extracted_data.append(record)

	extracted_data = extracted_data[1:]
	formatted_matrix = create_float_matrix(extracted_data)

	return formatted_matrix

def create_float_matrix(data):
	for entry in extracted_data:
		entry = [float(i) for i in entry]
		entry.pop(0)
		formatted_matrix.append(entry)
		
	formatted_matrix = np.matrix(formatted_matrix)
	formatted_matrix = formatted_matrix.astype(np.float)
	return formatted_matrix

# training data
X = getData('output/training_x.csv')
Y = getData('output/training_y.csv')

#Validation
X_validation = getData('output/test_x.csv')
Y_validation = getData('output/test_y.csv')

W = np.zeros(6)
W = np.matrix(W)
W = np.transpose(W)
W = W.astype(np.float)

output_matrix = []

def sigmoid(wT, x):
	x = np.transpose(x)
	wTx=np.dot(wT, x)
	wTxScalar = np.asscalar(wTx)
	sigmoid = 1/(1+np.exp(-wTxScalar))
	return sigmoid

# minimize cross-entropy error function
def log_likelihood(W, X, Y):
	log_likelihood = 0.0
	wT = np.transpose(W)
	for(x, y) in zip(X, Y):
		sigmoid = sigmoid(wT, x)
		y = np.asscalar(y)
		log_likelihood += (y*np.log(sigmoid)+(1-y)*np.log(1-sigmoid))
	return -log_likelihood

# deriviative of the log-likelihood function
def error_derivative(W, X, Y):
	sum = 0.0
	wT = np.transpose(W)
	for(x, y) in zip(X, Y):
		xT = np.transpose(x)
		partialProd = np.dot(xT, np.asscalar(y) - sigmoid(wT, x))
		sum = sum + partialProd
	return sum

def normalize(M):
	normalized_matrix = (M - np.mean(M, axis=0)) / np.std(M, axis=0)
	return normalized_matrix

def gradient_descent(W, X, Y, alpha=0.0000001, tol=0.2):
	X = normalize(X)
	X = np.c_[np.ones(X.shape[0]),X]
	log_likelihood = log_likelihood_func(W, X, Y)
	iteration = 0
	difference = 1
	while(difference > tol):
		previous_likelihood = log_likelihood
		gradient = error_derivative(W, X, Y)
		W = W + alpha*gradient
		log_likelihood = log_likelihood_func(W, X, Y)
		difference = np.abs(previous_likelihood - log_likelihood)
		print "Iteration: " + str(iteration) + "Delta: " + str(difference) + "Error: " + str(log_likelihood)
		iteration+=1
	return W

# NEED TO CHANGE THAT
def print_metrics(W, X, Y):
	counter = 0
	correctComing = 0
	guessComing = 0
	wT = np.transpose(W)
	log_likelihood = log_likelihood(W, X, Y)
	for (xi, y) in zip(X, Y):
		result = sigmoid(wT, xi)
		if (result >= 0.5):
			output_matrix.append(1)
			guessComing += 1
		else:
			output_matrix.append(0)
			if result >= 0.5 and y==1:
				correctComing += 1

			if (result >= 0.5 and y==1) or (result < 0.5 and y == 0):
				counter += 1

	successrate = 100*(float(counter)/float(len(X)))
	print "Guessed " + str(guessComing) + " are coming, " + str(correctComing) + " are correct."
	print "Accuracy Rate: " + str(successrate) + "%"
	#print_predicted_attendance(output_matrix, Y)

def main(X, Y, W):
	randomize = np.arange(len(x))
	np.random.shuffle(randomize)
	X = X[randomize]
	Y = Y[randomize]

	W = gradient_descent(W, X, Y)
	print_metrics(W, X, Y)
	print W


main(X, Y, W)
