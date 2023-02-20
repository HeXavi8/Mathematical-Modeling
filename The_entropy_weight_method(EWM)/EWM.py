import pandas as pd
import numpy as np
import math
from numpy import array

# Read the data
df = pd.read_csv('ewm.csv', encoding='gb2312')
# Preliminary data, remove records with null values
df.dropna()


# Define the EWM function
def ewm(df):
    df = df.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))
    rows, cols = df.shape
    k = 1.0 / math.log(rows)

    p = df / df.sum(axis=0)
    lnf = -np.log(p, where=df != 0) * p * k

    d = 1 - lnf.sum(axis=0)
    w = d / d.sum()

    w = pd.DataFrame(w)
    w = w.round(5)
    w.index = df.columns
    w.columns = ['weight']
    return w


if __name__ == '__main__':
    # Calculate the weight of each field of df
    w = ewm(df)  # Call cal_weight
    print(w)
    print('finish!')

