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
import numpy as np
import helpers

FILENAME = "data/Project1_data.csv"
OUTPUT_BASE = "output/"
Id = "Id"
NAME = "Name"
AGE = "Age Category"
SEX = "Sex"
RANK = "Rank"
TIME = "Time"
YEAR = "Year"
AGE_BINS = [11, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
COLS = [Id, NAME, AGE, SEX, RANK, TIME, YEAR]

helpers.init_pandas(pd, np)

# Preprocessing
# Remove Unknown genders, convert time to seconds and remove years earlier than 2007
df = pd.read_csv(FILENAME, usecols=COLS) \
    .greater_than(YEAR, 2007) \
    .not_equals(SEX, "U") \
    .convert_time() \
    .cut(AGE, AGE_BINS) \
    .remove_duplicate_runners(COLS)

helpers.save_groups(OUTPUT_BASE, df.groupby([AGE]))