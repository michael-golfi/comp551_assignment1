"""
COMP 551 - Assignment 1
Marathon Analysis

Data taken from:
https://www.athlinks.com/Events/383053/Courses/570971/

Authors:
    Michael Golfi <michael.golfi@mail.mcgill.ca>
    Ralph Bou-Samra <ralph.bou-samra@mcgill.ca>
    Sneha Desai <sneha.desai@mail.mcgill.ca>

Columns:
    Id Name Age Category Sex Rank Time Year
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import helpers
 
FILENAME = "data/Project1_data.csv"
OUTPUT_BASE = "output/"
Id = "Id"
AGE = "Age Category"
SEX = "Sex"
RANK = "Rank"
TIME = "Time"
YEAR = "Year"
PARTICIPATED = "Participated"
AGE_BINS = [11, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
COLS = [Id, AGE, SEX, RANK, TIME, YEAR]
TRAINING_THRESHOLD = 0.7

helpers.init_pandas(pd, np)

print "Preprocessing data"
# Remove Unknown genders, convert time to seconds and remove years earlier than 2007
df = pd.read_csv(FILENAME, usecols=COLS) \
    .not_equals(SEX, "U") \
    .convert_time() \
    .cut(AGE, AGE_BINS) \
    .remove_duplicate_runners(COLS)
    #.greater_than(YEAR, 2007) \
""" 
Questions:
    a. Predict Y1 using logistic regression, optimized with gradient descent.
    b. Predict Y1 using a Naive Bayes classifier.
    c. Predict Y2 using linear regression, optimized in closed-form or with gradient descent (with or without regularization).
"""
print "Splitting data to train and test sets"
cutoff = np.random.rand(len(df)) < TRAINING_THRESHOLD
train = df[cutoff]
test = df[~cutoff]

train = train[train[YEAR] != 2013]
test = test[test[YEAR] != 2013]

print "Generating Training Data Y for Y2"
train[train[YEAR] == 2016].to_csv(OUTPUT_BASE + "Y2Y_train.csv")
test[test[YEAR] == 2016].to_csv(OUTPUT_BASE + "Y2Y_test.csv")

print "Pivot training to list participants and years participated"
train[PARTICIPATED] = train[RANK].apply(lambda x: 1)
pivot_time = train.pivot_table(index=[Id], columns=[YEAR], values=PARTICIPATED, fill_value=0)
dedupes = train.groupby([Id]).last()
avgRank = train.groupby([Id]).apply(lambda x: x[RANK].mean())
avgTime = train.groupby([Id]).apply(lambda x: x[TIME].mean())

dedupes[AGE] = dedupes[AGE].astype('category') \
    .cat.codes.astype(int)
pivot_time[AGE] = dedupes[AGE] / dedupes[AGE].max()
pivot_time[SEX] = dedupes[SEX].apply(lambda x: 0 if x == 'M' else 1)
pivot_time[RANK] = avgRank.values / avgRank.values.max()
pivot_time[TIME] = avgTime.values / avgTime.values.max()

pivot_time = pivot_time[[SEX, AGE, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2014, 2015, 2016, RANK, TIME]]

test[PARTICIPATED] = test[RANK].apply(lambda x: 1)
pivot_test = test.pivot_table(index=[Id], columns=[YEAR], values=PARTICIPATED, fill_value=0)
dedupes = test.groupby([Id]).last()
avgRank = test.groupby([Id]).apply(lambda x: x[RANK].mean())
avgTime = test.groupby([Id]).apply(lambda x: x[TIME].mean())

dedupes[AGE] = dedupes[AGE].astype('category') \
    .cat.codes.astype(int)
pivot_test[AGE] = dedupes[AGE] / dedupes[AGE].max()
pivot_test[SEX] = dedupes[SEX].apply(lambda x: 0 if x == 'M' else 1)
pivot_test[RANK] = avgRank.values / avgRank.values.max()
pivot_test[TIME] = avgTime.values / avgTime.values.max()

pivot_test = pivot_test[[SEX, AGE, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2014, 2015, 2016, RANK, TIME]]

def addLastRace(pivotTable):
    lastYears = []
    for record in pivotTable.iterrows():
        lastYear = 0
        
        # Start from 2015 down since we need to test for 2016
        for year in [2015, 2014, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003]:
            if record[1].loc[year] == 1:
                break
            lastYear=lastYear+1
        lastYears.append(lastYear)
    pivotTable["LastRace"] = lastYears

print "Finding total races per participants and last race participated in"
pivot_time["TotalRaces"] = pivot_time[[2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2014, 2015]].sum(axis=1)
pivot_time["TotalRaces"] = pivot_time["TotalRaces"] / pivot_time["TotalRaces"].max()
addLastRace(pivot_time)
pivot_time["LastRace"] = pivot_time["LastRace"] / pivot_time["LastRace"].max()

pivot_test["TotalRaces"] = pivot_test[[2003, 2004, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2014, 2015]].sum(axis=1)
pivot_test["TotalRaces"] = pivot_test["TotalRaces"] / pivot_test["TotalRaces"].max()
addLastRace(pivot_test)
pivot_test["LastRace"] = pivot_test["LastRace"] / pivot_test["LastRace"].max()






print "Generating Training Data X for Y2"
#train = train[train[2016] == 1]
#train[[SEX, AGE, 2008, 2009, 2010, 2011, 2012, 2014, 2015, TIME, RA NK,  "TotalRaces", "LastRace"]].to_csv(OUTPUT_BASE + "lalala.csv")
train2 = pivot_time[pivot_time[2016] == 1]
train2.to_csv(OUTPUT_BASE + "Y2X_train.csv")

train3 = pivot_test[pivot_test[2016] == 1]
train3.to_csv(OUTPUT_BASE + "Y2X_test.csv")



#train[2016].to_csv(OUTPUT_BASE + "training_y.csv")




