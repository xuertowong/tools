import pandas as pd
from pandas import DataFrame, Series
import os,sys
import re

def select(address,parttern1,pattern2):
    list1 = os.listdir(address)
    list1 = Series(list1)
    c = list1.str.contains(parttern1)
    for i in range(len(c)):
        if c[i] == True:
            data = pd.read_csv(address+list1[i])
            data = data[data[data.columns[0]].str.contains(pattern2]
            data.to_csv(address+'1'+list1[i])
            