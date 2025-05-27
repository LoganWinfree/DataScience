import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import sklearn.metrics as skm
import math

reg = linear_model.LinearRegression()

data = pd.read_csv("DataScience/Student Habits/student_habits_performance.csv")
data = pd.get_dummies(data, columns=["gender", "part_time_job", "diet_quality", "parental_education_level", "internet_quality", "extracurricular_participation"], drop_first=True)
x = data.drop('exam_score', axis=1).drop('student_id', axis=1)
y = data['exam_score']

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1)

reg.fit(train_x, train_y)

predict_y = reg.predict(test_x)

print("R Square: ") 
print(round(skm.r2_score(test_y, predict_y), 3))
print("\nRoot MSE: ")
print(round(skm.root_mean_squared_error(test_y, predict_y), 3))