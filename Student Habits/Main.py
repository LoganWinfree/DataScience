import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

data = pd.read_csv("DataScience/Student Habits/student_habits_performance.csv")

x = data.drop('exam_score', axis=1)
y = data['exam_score']

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1)

