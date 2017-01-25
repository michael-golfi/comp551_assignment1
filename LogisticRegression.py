import numpy as np
import pandas as pd
import csv
import math
from decimal import *
import matplotlib.pyplot as plt
import random


def getCSVAndFormat(CSVF_name):
	targetMatrix = []
	temp = []
	with open(CSVF_name,'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			temp.append(row)

	temp = temp[1:]

	for entry in temp:
		entry = [float(i) for i in entry]
		entry.pop(0)
		targetMatrix.append(entry)

	targetMatrix = np.matrix(targetMatrix)
	targetMatrix = targetMatrix.astype(np.float)

	return targetMatrix


#Training 
X = getCSVAndFormat('trainX.csv')
Y = getCSVAndFormat('trainY.csv')

#Validation
Xval = getCSVAndFormat('valX.csv')
Yval = getCSVAndFormat('valY.csv')


W = np.zeros(6)
W = np.matrix(W)
W = np.transpose(W)
W = W.astype(np.float)

Z = []


def sigmoid(wT, x):
	x = np.transpose(x)
	wTx=np.dot(wT, x)
	wTxScalar = np.asscalar(wTx)
	sigmoid = 1/(1+np.exp(-wTxScalar)
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

def gradient_descent(W, X, Y, alpha=0.0000001, tol=0.2):
	#normalizing needs to go in here
	log_likelihood = log_likelihood(W, X, Y)
	iteration = 0
	difference = 1
	while(difference > tol):
		previous_likelihood = log_likelihood
		gradient = error_derivative(W, X, Y)
		W = W + alpha*gradient
		log_likelihood = log_likelihood(W, X, Y)
		difference = np.abs(previous_likelihood - log_likelihood)
		print "Iteration: " + str(i) + "Delta: " + str(difference) + "Error: " + str(log_likelihood)
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
			Z.append(1)
			guessComing += 1
		else:
			Z.append(0)
			if result >= 0.5 and y==1:
				correctComing += 1

			if (result >= 0.5 and y==1) or (result < 0.5 and y == 0):
				counter += 1

	successrate = 100*(float(counter)/float(len(X)))
	print "Guessed " + str(guessComing) + " are coming, " + str(correctComing) + " are correct."
	print "Accuracy Rate: " + str(successrate) + "%"
	#print_predicted_attendance(Z, Y)

def main(X, Y, W):
	randomize = np.arrange(len(x))
	np.random.shuffle(randomize)
	X = X[randomize]
	Y = Y[randomize]

	W = gradient_descent(W, X, Y)
	print_metrics(W, X, Y)
	print W


main(X, Y, W)