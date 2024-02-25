import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("dataset.csv", index_col=0)

# Find students/rows where either mother or father graduated high school AND student was enrolled in >0 units first sem
highschool = students[(students["Mother's qualification"] == 1) | (students["Father's qualification"] == 1) & (
students["Curricular units 1st sem (enrolled)"] > 0)]

# Function that takes a list of the parent qualifications (quals) by which you are trying to filter and finds all rows
# where either Mother OR Father has one of those qualifications AND where student is enrolled in >0 units 1st sem
def grade1ByQuals(quals):
    filtGroup = students[(students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(
    quals)) & (students["Curricular units 1st sem (enrolled)"] > 0)]
    avgGrade = filtGroup['Curricular units 1st sem (grade)'].mean()
    return avgGrade

avgGrade_MS = grade1ByQuals([9, 10, 13, 14, 19, 29])
avgGrade_HS = grade1ByQuals([1])
avgGrade_Bach = grade1ByQuals([2])
avgGrade_Mast = grade1ByQuals([4, 43])
avgGrade_Doc = grade1ByQuals([5, 44])

# For those students/rows filtered above, find average of first sem avg grade
avg_grade = myinfo['Curricular units 1st sem (grade)'].mean()
print(avg_grade)

