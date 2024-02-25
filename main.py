import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("dataset.csv", index_col=0)

# Find students/rows where either mother or father graduated high school AND student was enrolled in >0 units first sem
highschool = students[(students["Mother's qualification"] == 1) | (students["Father's qualification"] == 1) & (
students["Curricular units 1st sem (enrolled)"] > 0)]

# Function that takes a list of the parent qualifications (quals) by which you are trying to filter and finds all rows
# where either Mother OR Father has one of those qualifications AND where student is enrolled in >0 units 1st sem
define filtByQua
students[(students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(
quals)) & (students["Curricular units 1st sem (enrolled)"] > 0)]

highschool
bachelors
masters
doctorate

# For those students/rows filtered above, find average of first sem avg grade
avg_grade = myinfo['Curricular units 1st sem (grade)'].mean()
print(avg_grade)

