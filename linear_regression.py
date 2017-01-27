import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
import datetime

AGE = "Age Category"
SEX = "Sex"
TIME = "Time"
OUTPUT_BASE = "output/"

COLS_X = [AGE, SEX, TIME, "TotalRaces"]
COLS_Y = [TIME]

#training data
TRAIN_X = "output/Y2X_train.csv"
TRAIN_Y = "output/Y2Y_train.csv"

#testing data
TEST_X = "output/Y2X_test.csv"
TEST_Y = "output/Y2Y_test.csv"

#Prediction data
PREDICTION = "output/PREDICTION.csv"

#Read preprocessed data
df_X_train = pd.read_csv(TRAIN_X, usecols=COLS_X) 
df_Y_train = pd.read_csv(TRAIN_Y, usecols=COLS_Y)

#Read test data
df_X_test = pd.read_csv(TEST_X, usecols=COLS_X)
df_Y_test = pd.read_csv(TEST_Y, usecols=COLS_Y)

df_2017 = pd.read_csv(PREDICTION, usecols=COLS_X)

#Closed form solution: w = (XTX)^(-1)XTY
a = np.linalg.inv(np.dot(df_X_train.as_matrix().transpose(),df_X_train.as_matrix()))
b = np.dot(df_X_train.as_matrix().transpose(),df_Y_train.as_matrix())
w = np.dot(a,b)

y = np.dot(df_X_test, w)

print w 
print abs((y-df_Y_test.as_matrix())).mean()
print (y-df_Y_test.as_matrix()).max()

a = abs(((y-df_Y_test.as_matrix())/df_Y_test.as_matrix())*100)
print a.max()
print a.mean()
c=0

for threshold in range(0,21):
	for i in range(len(a)):
		if a[i] < threshold:
			c = c + 1
     
	d = (float(c)/float(len(a)))*100

	print threshold,d
	c = 0


  
y_2017 = np.dot(df_2017,w)

new_time = list()

for i in range(len(y_2017)):
	m, s = divmod(y_2017[i], 60)
	h, m = divmod(m, 60)
	new_time.append("%d:%02d:%02d" % (h, m, s))

pd.DataFrame(new_time).to_csv(OUTPUT_BASE + "LR_Results.csv")


















