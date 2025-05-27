import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import sklearn.metrics as skm
import sklearn.preprocessing as prep
import math

reg = linear_model.LogisticRegression(max_iter=1000)

le = prep.LabelEncoder().fit(["positive", "negative"])

data = pd.read_csv("DataScience/Heart Attack/Medicaldataset.csv")

x = data.drop("Result", axis=1)
y = data["Result"]

y_new = le.fit_transform(y)
y_new = np.transpose(y_new)

train_x, test_x, train_y, test_y = train_test_split(x, y_new, test_size=0.1)

scale = prep.StandardScaler()
train_x = scale.fit_transform(train_x)
test_x = scale.transform(test_x)

reg.fit(train_x, train_y)

predict_y = reg.predict(test_x)
print("Accuracy: ")
print(round(skm.accuracy_score(test_y, predict_y), 3))
print("\nR Square: ") 
print(round(skm.r2_score(test_y, predict_y), 3))
print("\nRoot MSE: ")
print(round(skm.root_mean_squared_error(test_y, predict_y), 3))