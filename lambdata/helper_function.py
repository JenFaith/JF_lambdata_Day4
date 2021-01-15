"""Lambdata - A collection of Data Science Helper Functions """
"""A collection of helper functions"""
import numpy as np 
import pandas as pd
import sklearn
from sklearn.utils import shuffle
import random

class NullCount(pd.DataFrame):
    """Counts number of Null Values in a DataFrame"""
    def null_count(self):
        return self.isna().sum().sum()


class Radomize:
    """Return a randomized dataframe"""
    def __init__(self, df, seed):
        self.df = df
        self.seed = seed
        
    def randomize(self):
        df_n = shuffle(self.df, random_state = self.seed)
        return df_n
    

print('Working As Expected')