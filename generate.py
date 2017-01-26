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
    .greater_than(YEAR, 2007) \
    .not_equals(SEX, "U") \
    .convert_time() \
    .cut(AGE, AGE_BINS) \
    .remove_duplicate_runners(COLS) \
    .reigel()

print df[df[YEAR] == 2013]

""" 
Questions:
    a. Predict Y1 using logistic regression, optimized with gradient descent.
    b. Predict Y1 using a Naive Bayes classifier.
    c. Predict Y2 using linear regression, optimized in closed-form or with gradient descent (with or without regularization).
"""

print "Pivot data to list participants and years participated"
df[PARTICIPATED] = df[RANK].apply(lambda x: 1)
pivot = df.pivot_table(index=[Id], columns=[YEAR], values=PARTICIPATED, fill_value=0)
dedupes = df.groupby([Id]).last()
avgRank = df.groupby([Id]).apply(lambda x: x[RANK].mean())
avgTime = df.groupby([Id]).apply(lambda x: x[TIME].mean())

dedupes[AGE] = dedupes[AGE].astype('category') \
    .cat.codes.astype(int)
pivot[AGE] = dedupes[AGE] / dedupes[AGE].max()
pivot[SEX] = dedupes[SEX].apply(lambda x: 0 if x == 'M' else 1)
pivot[RANK] = avgRank.values / avgRank.values.max()
pivot[TIME] = avgRank.values / avgRank.values.max()

pivot = pivot[[SEX, AGE, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, RANK, TIME]]

def addLastRace(pivotTable):
    lastYears = []
    for record in pivotTable.iterrows():
        lastYear = 1
        
        # Start from 2015 down since we need to test for 2016
        for year in [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008]:
            if record[1].loc[year] == 1:
                break
            lastYear=lastYear+1
        lastYears.append(lastYear)
    pivotTable["LastRace"] = lastYears

print "Finding total races per participants and last race participated in"
pivot["TotalRaces"] = pivot[[2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]].sum(axis=1)
pivot["TotalRaces"] = pivot["TotalRaces"]
addLastRace(pivot)
pivot["LastRace"] = pivot["LastRace"]

print "Splitting data to train and test sets"
cutoff = np.random.rand(len(pivot)) < TRAINING_THRESHOLD
train = pivot[cutoff]
test = pivot[~cutoff]

print "Finding those who participanted in 2016 and those who did not"
participated2016 = (train.xs(2016, axis=1, drop_level=False) == 1).as_matrix()
participantsIn2016 = train[participated2016]
nonParticipantsIn2016 = train[~participated2016]

print "Generating Training Data"
#train[[SEX, AGE, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, TIME, RANK,  "TotalRaces", "LastRace"]].to_csv(OUTPUT_BASE + "training_x.csv")
train[[AGE, 2015, "TotalRaces", RANK, "LastRace"]].to_csv(OUTPUT_BASE + "train_x.csv")
train[2016].to_csv(OUTPUT_BASE + "train_y.csv")

print "Generating Test Data"
#test[[SEX, AGE, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, TIME, RANK, "TotalRaces", "LastRace"]].to_csv(OUTPUT_BASE + "test_x.csv")
test[[AGE, 2015, "TotalRaces", RANK, "LastRace"]].to_csv(OUTPUT_BASE + "test_x.csv")
test[2016].to_csv(OUTPUT_BASE + "test_y.csv")