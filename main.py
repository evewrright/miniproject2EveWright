import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("dataset.csv", index_col=0)

# Find students/rows where either mother or father graduated high school AND student was enrolled in >0 units first sem
#highschool = students[(students["Mother's qualification"] == 1) | (students["Father's qualification"] == 1) & (
#students["Curricular units 1st sem (enrolled)"] > 0)]

# Function that takes a list of the parent qualifications (quals) by which you are trying to filter and finds all rows
# where either Mother OR Father has one of those qualifications AND where student is enrolled in >0 units 1st sem
def grade1ByQuals(quals):
    filtGroup = students[(students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(
    quals)) & (students["Curricular units 1st sem (enrolled)"] > 0)]
    avgGrade = filtGroup['Curricular units 1st sem (grade)'].mean()
    return avgGrade

# Exact same as above function but for 2nd semester grades
def grade2ByQuals(quals):
    filtGroup = students[(students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(
    quals)) & (students["Curricular units 2nd sem (enrolled)"] > 0)]
    avgGrade = filtGroup['Curricular units 2nd sem (grade)'].mean()
    return avgGrade

# Function that takes a list of qualifications and finds all rows where the quals are true for BOTH parents
# and where student enrolled in >0 units. Then finds average of average grade
def grade2Both(quals):
    filtGroup = students[(students["Mother's qualification"].isin(quals)) & (students["Father's qualification"].isin(
    quals)) & (students["Curricular units 2nd sem (enrolled)"] > 0)]
    avgGrade = filtGroup['Curricular units 2nd sem (grade)'].mean()
    return avgGrade

# Call grade1 function to gather data to plot
avgGrade_MS = grade1ByQuals([9, 10, 13, 14, 19, 29])
avgGrade_HS = grade1ByQuals([1])
avgGrade_Bach = grade1ByQuals([2])
avgGrade_Mast = grade1ByQuals([4])
avgGrade_Doc = grade1ByQuals([5])

quals = ['Middle School', 'High School', "Bachelor's", "Master's", "Doctorate"]
avgGrades = [avgGrade_MS, avgGrade_HS, avgGrade_Bach, avgGrade_Mast, avgGrade_Doc]

plt.bar(quals, avgGrades)
plt.ylim(min(avgGrades) - .5, max(avgGrades) + .5)
plt.ylabel('Mean Average Student Grade of 1st Semester Units')
plt.xlabel("Parental Education of at least 1 Parent")
plt.title("Mean of Average 1st Semester Grades by Level of Parent Education")
plt.show()


# Call grade2 function to gather data to plot
avgGrade2_MS = grade2ByQuals([9, 10, 13, 14, 19, 29])
avgGrade2_HS = grade2ByQuals([1])
avgGrade2_Bach = grade2ByQuals([2])
avgGrade2_Mast = grade2ByQuals([4])
avgGrade2_Doc = grade2ByQuals([5])

avgGrades2 = [avgGrade2_MS, avgGrade2_HS, avgGrade2_Bach, avgGrade2_Mast, avgGrade2_Doc]

plt.bar(quals, avgGrades2)
plt.ylim(min(avgGrades2) - .5, max(avgGrades2) + .5)
plt.ylabel('Mean Average Grade of 2nd Semester Units')
plt.xlabel("Parental Education of at least 1 Parent")
plt.title("Mean of Average 2nd Semester Grades by Parental Education")
plt.show()


# Find avg 2nd sem grade by parent ed of BOTH parents
#avgGrade2_MS = grade2ByQuals([9, 10, 13, 14, 19, 29])
avgGrade2_HS = grade2ByQuals([1]) ---where one has HS and other has HS or higher
avgGrade2_Bach = grade2ByQuals([2], [2, 4, 5]) ---where 1 has bach and other has bach or higher
avgGrade2_Mast = grade2ByQuals([4]) ---where 1 has masters and other has masters or higher
avgGrade2_Doc = grade2ByQuals([5])

def grade2Both(quals1, quals2):
    filtGroup = students[(students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(
    quals)) & (students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(
    quals)) & (students["Curricular units 2nd sem (enrolled)"] > 0)]
    avgGrade = filtGroup['Curricular units 2nd sem (grade)'].mean()
    return avgGrade
check that both have bachelors or higher ----
students[(students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(quals))

check that one has bachelors----



avgGrades2 = [avgGrade2_MS, avgGrade2_HS, avgGrade2_Bach, avgGrade2_Mast, avgGrade2_Doc]

plt.bar(quals, avgGrades2)
plt.ylim(min(avgGrades2) - .5, max(avgGrades2) + .5)
plt.ylabel('Mean Average Grade of 2nd Semester Units')
plt.xlabel("Parental Education of at least 1 Parent")
plt.title("Mean of Average 2nd Semester Grades by Parental Education")
plt.show()


