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

In order to generate the data:

```bash
python generate.py
```

## Predicting Participation

### Logistic Regression

```bash
python LogisticRegression.py
```

### Gaussian Naive Bayes

The files train\_x.csv, train\_y.csv, test\_x.csv and test\_y.csv must be available from the generate step.

```bash
python naive_bayes.py
```
## Predicting Time

```bash
python generate_prediction.py
```