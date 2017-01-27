import pandas as pd
import numpy as np
import math


allColumns = [["Sex", "Age Category", "Rank", "Time", "TotalRaces"]]
def gauss(x, mean, std):
    return np.float64((1 / (math.sqrt(2 * math.pi) * std**2)) * math.exp(-((x-mean)**2/(2*std**2))))

def predictDistribution(trueAvgStd, falseAvgStd, input):
    """
    Decision method: Will the input be participating or not?
    """    
    willParticipate = np.float64(1.0)
    wontParticipate = np.float64(1.0)

    for i in range(len(trueAvgStd)):
        mean,std = trueAvgStd[i]
        x = input[i]
        res = gauss(x, mean, std)
        
        willParticipate *= res

    for i in range(len(falseAvgStd)):
        mean,std = falseAvgStd[i]
        x = input[i]
        wontParticipate *= gauss(x, mean, std)

    if willParticipate > wontParticipate:
        return 1
    else:
        return 0

def runAll(trueAvgStd, falseAvgStd, instances):
    results = []
    for instance in instances:
        predict = predictDistribution(trueAvgStd, falseAvgStd, instance)
        results.append(predict)
    return results

def calculateAccuracy(prediction, test):
    trueInstances = 0
    testSize = len(test)
    for i in range(testSize):
        if prediction[i] == test[i][-1]:
            trueInstances += 1
    
    # Return an accuracy in percent
    return (trueInstances/float(testSize)) * 100.0

print "Loading training data"
train_x = pd.read_csv("output/training_x.csv")
train_y = pd.read_csv("output/train_y.csv")

print "Loading validation data"
test_x = pd.read_csv("output/test_x.csv")
test_y = pd.read_csv("output/test_y.csv")

didParticipate = (train_x.xs("2015", axis=1, drop_level=False) == 1).as_matrix()

columns = allColumns[0]

print "Finding those who participanted in 2016 and those who did not"
participants2015 = train_x[columns][didParticipate].as_matrix()
nonParticipants2015 = train_x[columns][~didParticipate].as_matrix()

print "Zipped Averages and Standard Deviations as [(Average, StdDev), ...]"
participatedAvg = participants2015.mean(axis=0)
participatedStd = participants2015.std(axis=0, ddof=1)

nonParticipatedAvg = participants2015.mean(axis=0)
nonParticipatedStd = nonParticipants2015.std(axis=0, ddof=1)

participatedVector = zip(participatedAvg, participatedStd)
nonParticipatedVector = zip(nonParticipatedAvg, nonParticipatedStd)

testX = test_x[columns].as_matrix()
testY = test_y.as_matrix()

results = runAll(participatedVector, nonParticipatedVector, testX)
#print results
acc = calculateAccuracy(results, testY)
print columns, acc

print "Training on 2016 dataset"

predictionSet = pd.read_csv("output/pivot.csv")
didParticipate = (predictionSet.xs("2016", axis=1, drop_level=False) == 1).as_matrix()

print "Finding those who participanted in 2016 and those who did not"
participants2016 = predictionSet[columns][didParticipate].as_matrix()
nonParticipants2016 = predictionSet[columns][~didParticipate].as_matrix()

participatedAvg = participants2016.mean(axis=0)
participatedStd = participants2016.std(axis=0, ddof=1)

nonParticipatedAvg = nonParticipants2016.mean(axis=0)
nonParticipatedStd = nonParticipants2016.std(axis=0, ddof=1)

participatedVector = zip(participatedAvg, participatedStd)
nonParticipatedVector = zip(nonParticipatedAvg, nonParticipatedStd)

testX = predictionSet[columns].as_matrix()

results = runAll(participatedVector, nonParticipatedVector, testX)
print "Predictions for 2017"
print results
print "Recurrences: ", sum(results)