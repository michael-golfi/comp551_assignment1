"""

COMP 551 - Assignment 1
Marathon Analysis

Data taken from:
https://www.athlinks.com/Events/383053/Courses/570971/

"""

# Authors: Michael Golfi <michael.golfi@mail.mcgill.ca>, Ralph Bou-Samra <ralph.bou-samra@mcgill.ca> Sneha Desai <sneha.desai@mail.mcgill.ca>
# License: MIT

import pandas as pd
import numpy as np

def init_print():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

def print_groupby(grouped):
    for key, item in grouped:
        print key
        print grouped.get_group(key), "\n"

init_print()

ageCategories = [11, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
df = pd.read_csv('data/data.csv')
del df["Name"]
df["Age Category"] = pd.cut(df['Age Category'], 
    bins=ageCategories, 
    include_lowest=True, 
    right=False)

grouped = df.groupby(['Age Category', 'Sex'])

print_groupby(grouped)