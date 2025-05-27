import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import sklearn.metrics as skm
import math

reg = linear_model.LogisticRegression()

data = pd.read_csv("DataScience/Heart Attack/Medicaldataset.csv")
