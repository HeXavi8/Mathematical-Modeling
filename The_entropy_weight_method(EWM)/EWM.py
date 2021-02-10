import pandas as pd
import numpy as np
import math
from numpy import array
 
# Read the data
df = pd.read_csv('ewm.csv', encoding='gb2312')
# Preliminary data, remove records with null values
df.dropna()
 
#Define the EWM function
def cal_weight(x):
    '''calculate the weight of variables'''
    # standardized
    x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))
 
    # Calculate k
    rows = x.index.size  # row
    cols = x.columns.size  # column
    k = 1.0 / math.log(rows)
 
    lnf = [[None] * cols for i in range(rows)]
 
    # Matrix calculation
    # Information entropy
    # p=array(p)
    x = array(x)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    E = lnf
 
    # Calculate redundancy
    d = 1 - E.sum(axis=0)
    # Calculate the weight of each indicator
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / sum(d)
        w[j] = wj
        # Calculate the comprehensive score of each sample, using the most original data
    
    w = pd.DataFrame(w)
    return w
 
 
if __name__ == '__main__':
    # Calculate the weight of each field of df
    w = cal_weight(df)  # Call cal_weight
    w.index = df.columns
    w.columns = ['weight']
    print(w)
    print('finish!')
 
