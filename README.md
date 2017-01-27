# comp551_assignment1
Implementation of Linear Regression Predictor

## Preprocessing

The preprocessing stage: 
- Removes the pace column
- Filters out unknown genders
- Removes the 2013 data
- Converts the time to a numerical format
- Organizes the ages into group ranges
- Removes duplicates among years by averaging their results

In order to generate the data for Y1-naive bayes:

```bash
python generate-naive.py
```

In order to generate the data for Y1-logistic regression:

```bash
python generate-logistic.py
```

In order to generate the data for Y2:

```bash
python generate_Y2.py
```

In order to generate the data for futrue Prediction:

```bash
python generate_PREDICTION.py
```
## Predicting Participation

### Logistic Regression

The files training_x.csv, training_y.csv, test_x.csv and test_y.csv must be available from the generate Y1-logistic step.

```bash
python LogisticRegression.py
```

### Gaussian Naive Bayes

The files train\_x.csv, train\_y.csv, test\_x.csv and test\_y.csv must be available from the generate Y1-naive step.

```bash
python naive_bayes.py
```
## Predicting Time

The files Y2Y_train.csv, Y2Y_test.csv, Y2X_test.csv, Y2X_train.csv must be avilable from the generate Y2 step.

```bash
python linear_regression.py
```


