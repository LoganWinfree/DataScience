import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import sklearn.metrics as skm
import math

data = pd.read_csv("DataScience/Heart Attack/Medicaldataset.csv")
print(data.head())