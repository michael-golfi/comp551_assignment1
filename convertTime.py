"""
Converts the given time from HH:MM:SS format to seconds
"""

import pandas as pd
import numpy as np
from pandas import DataFrame

def get_sec(time_str):
	h, m, s = time_str.split(':')
	return int(h) * 3600 + int(m) * 60 + int(s)

df = pd.read_csv('data/data.csv')
df['Time'] = df['Time'].apply(get_sec)
df.to_csv('data/data.csv')