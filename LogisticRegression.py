import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

W = np.zeros(19)
W = np.matrix(W)
W = np.transpose(W)
W = W.astype(np.float)

predictions = []

def getData(csv_file):
	formatted_matrix = []
	extracted_data = []
	# extract data
	with open(csv_file,'rb') as csvfile:
		reader = csv.reader(csvfile)
		for record in reader:
			extracted_data.append(record)
        # do not consider the first header row 
	extracted_data = extracted_data[1:]
	formatted_matrix = create_float_matrix(extracted_data)
	return formatted_matrix

def create_float_matrix(data):
	formatted_matrix = []
	for entry in data:
		# make sure the values are floats
		entry = [float(i) for i in entry]
		# remove the first row
		entry.pop(0)
		# add the matrices to the matrix
		formatted_matrix.append(entry)
		
	formatted_matrix = np.matrix(formatted_matrix)
	formatted_matrix = formatted_matrix.astype(np.float)
	return formatted_matrix

# training data
X = getData('output/training_x.csv')
Y = getData('output/training_y.csv')

# predictions
all_set = getData('output/PREDICTIONS.csv')

output_matrix = []
training_error = []

# logistic function
def sigmoid_func(wT, x):
	x = np.transpose(x)
	# dot product
	wTx = np.dot(wT, x)
	wTx = np.asscalar(wTx)
	sigmoid = 1/(1+np.exp(-wTx))
	return sigmoid

# minimize cross-entropy error function
def log_likelihood_func(X, Y, W):
	log_likelihood = 0.0
	wT = np.transpose(W)
	for(x, y) in zip(X, Y):
		sigmoid = sigmoid_func(wT, x)
		y = np.asscalar(y)
		log_likelihood += ((y*np.log(sigmoid))+((1.0-y)*np.log(1.0-sigmoid)))
	return -log_likelihood
# gaussian normalization
def normalize(M):
	normalized_matrix = (M - np.mean(M, axis=0)) / np.std(M, axis=0)
	return normalized_matrix
# add weights of one to the matrix
def addOnes(X):
	X = np.c_[np.ones(X.shape[0]),X]
	return X

def predict2017(W,X):
	X = normalize(X)
	X = addOnes(X)
	WT = np.transpose(W)
	for x in X:
		result = sigmoid_func(WT,x)
		if(result < 0.5):
			predictions.append(0)
		else:
			predictions.append(1)

def gradient_descent(W, X, Y, alpha=.00015, tol=0.5):
	iteration = 0
	difference = 1
	X = normalize(X)
	X = addOnes(X)
	# compute the error
	log_likelihood = log_likelihood_func(X, Y, W)
	while(difference > tol):
		previous_likelihood = log_likelihood
		gradient = 0.0
		wT = np.transpose(W)
		# calculate the error derivative
		for(x, y) in zip(X, Y):
			xT = np.transpose(x)
			partialGradProduct = np.dot(xT,np.asscalar(y) - sigmoid_func(wT, x))
			gradient += partialGradProduct

		W = W + alpha*gradient
		log_likelihood = log_likelihood_func(X, Y, W)
		training_error.append([iteration,log_likelihood])
		difference = previous_likelihood - log_likelihood
		print "Iteration: " + str(iteration) + " Error: " + str(log_likelihood)
		iteration+=1
	return W

def main(X, Y, W):
	W = gradient_descent(W, X, Y)
	print X
	print Y
	print W
	predict2017(W, all_set)
	
	("PREDICTION.csv","w") as csvfile:
		writer = csvfile.writer(fp,delimiter="\n")
		writer.writerow(predictions)

main(X, Y, W)
