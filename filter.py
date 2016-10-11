import pandas as pd
from pandas import DataFrame, Series
import os,sys
import re

def select(address,pattern2):
    list1 = os.listdir(address)
    list1 = Series(list1)
    for i in range(len(list1)):
        data = pd.read_csv(address+list1[i])
        data = data.dropna()
        data = data[data['gene'].str.contains(pattern2)]
        data.to_csv(address+'1'+list1[i])
            