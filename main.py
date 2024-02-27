import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("dataset.csv", index_col=0)


# Function that takes a list of the parent qualifications (quals) by which you are trying to filter and finds all rows
# where either Mother OR Father has one of those qualifications AND where student is enrolled in >0 units 1st sem
def grade1ByQuals(quals):
    filtGroup = students[(students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(
    quals)) & (students["Curricular units 1st sem (approved)"] > 0)]
    avgGrade = filtGroup['Curricular units 1st sem (grade)'].mean()
    return avgGrade

# Exact same as above function but for 2nd semester grades
def grade2ByQuals(quals):
    filtGroup = students[(students["Mother's qualification"].isin(quals)) | (students["Father's qualification"].isin(
    quals)) & (students["Curricular units 2nd sem (approved)"] > 0)]
    avgGrade = filtGroup['Curricular units 2nd sem (grade)'].mean()
    return avgGrade

# Function that takes a list of qualifications and finds all rows where the quals are true for BOTH parents
# and where student enrolled in >0 units. Then finds average of average grade in 1st sem
# where quals 1 is the [level or higher] and quals2 is [minimum level]
def grade1Both(quals1, quals2):
    filtGroup = students[(students["Mother's qualification"].isin(quals1)) & (students["Father's qualification"].isin(
    quals1)) & (students["Mother's qualification"].isin(quals2)) | (students["Father's qualification"].isin(
    quals2)) & (students["Curricular units 1st sem (approved)"] > 0)]
    avgGrade = filtGroup['Curricular units 1st sem (grade)'].mean()
    return avgGrade

# Exact same as above function grade1Both, but for 2nd semester grades
def grade2Both(quals1, quals2):
    filtGroup = students[(students["Mother's qualification"].isin(quals1)) & (students["Father's qualification"].isin(
    quals1)) & (students["Mother's qualification"].isin(quals2)) | (students["Father's qualification"].isin(
    quals2)) & (students["Curricular units 2nd sem (approved)"] > 0)]
    avgGrade = filtGroup['Curricular units 2nd sem (grade)'].mean()
    return avgGrade

def grade1ByAge(ages):
    filtGroup = students[(students["Age at enrollment"].isin(ages)) & (students["Curricular units 1st sem (approved)"] > 0)]
    avgGrade = filtGroup['Curricular units 1st sem (grade)'].mean()
    return avgGrade


# Find Avg 1st Semester Grades by At Least 1 Parent Qualification
avgGrade_MS = grade1ByQuals([9, 10, 12, 13, 14, 19, 29, 30])
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
plt.title("Average of 1st Semester Grades by Parental Education")
plt.show()


# Find Avg 2nd Semester Grades by At Least 1 Parent Qualification
avgGrade2_MS = grade2ByQuals([9, 10, 12, 13, 14, 19, 29, 30])
avgGrade2_HS = grade2ByQuals([1])
avgGrade2_Bach = grade2ByQuals([2])
avgGrade2_Mast = grade2ByQuals([4])
avgGrade2_Doc = grade2ByQuals([5])

avgGrades2 = [avgGrade2_MS, avgGrade2_HS, avgGrade2_Bach, avgGrade2_Mast, avgGrade2_Doc]

plt.bar(quals, avgGrades2)
plt.ylim(min(avgGrades2) - .5, max(avgGrades2) + .5)
plt.ylabel('Mean Average Grade of 2nd Semester Units')
plt.xlabel("Parental Education of at least 1 Parent")
plt.title("Average of 2nd Semester Grades by Parental Education")
plt.show()


# Find Avg 1st Semester Grade by Parent Qualification of BOTH parents
grade1Both_MS = grade1Both([1, 2, 4, 5, 9, 10, 12, 13, 14, 19, 29, 30], [9, 10, 12, 13, 14, 19, 29, 30])
grade1Both_HS = grade1Both([1, 2, 4, 5], [1])
grade1Both_Bach = grade1Both([2, 4, 5], [2])
grade1Both_Mast = grade1Both([4, 5], [4])
grade1Both_Doc = grade1Both([5], [5])

qualsBoth = ['Middle School', 'High School', "Bachelor's", "Master's", "Doctorate"]
avgGrades1Both = [grade1Both_MS, grade1Both_HS, grade1Both_Bach, grade1Both_Mast, grade1Both_Doc]

plt.bar(qualsBoth, avgGrades1Both, color='purple')
plt.ylim(min(avgGrades1Both) - .5, max(avgGrades1Both) + .5)
plt.ylabel('Mean Average Grade of 1st Semester Units')
plt.xlabel("Parental Education of Both Parents")
plt.title("Average of 1st Semester Grades by BOTH Parental Education")
plt.show()


# Find Avg 2nd Semester Grade by Parent Qualification of BOTH parents
grade2Both_MS = grade2Both([1, 2, 4, 5, 9, 10, 12, 13, 14, 19, 29, 30], [9, 10, 12, 13, 14, 19, 29, 30])
grade2Both_HS = grade2Both([1, 2, 4, 5], [1])
grade2Both_Bach = grade2Both([2, 4, 5], [2])
grade2Both_Mast = grade2Both([4, 5], [4])
grade2Both_Doc = grade2Both([5], [5])

avgGrades2Both = [grade2Both_MS, grade2Both_HS, grade2Both_Bach, grade2Both_Mast, grade2Both_Doc]

plt.bar(qualsBoth, avgGrades2Both, color='purple')
plt.ylim(min(avgGrades2Both) - .5, max(avgGrades2Both) + .5)
plt.ylabel('Mean Average Grade of 2nd Semester Units')
plt.xlabel("Parental Education of Both Parents")
plt.title("Average of 2nd Semester Grades by BOTH Parental Education")
plt.show()


# Finds Avg 2nd Semester Grades by Age at Enrollment and then graphs grouped by gender
filtGroup = students[students["Curricular units 2nd sem (approved)"] > 0]
women = filtGroup[filtGroup['Gender'] == 0]
men = filtGroup[filtGroup['Gender'] == 1]
avgGradeW = women.groupby(['Age at enrollment'])['Curricular units 2nd sem (grade)'].mean()
avgGradeM = men.groupby(['Age at enrollment'])['Curricular units 2nd sem (grade)'].mean()

avgGradeW.plot(color='red', label='Women', marker='o')
avgGradeM.plot(color='blue', label='Men', marker='o')
plt.xlim(17, 28)
plt.ylim(11.75, 14)
plt.title('Average 2nd Semester Grades by Age at Enrollment, Grouped by Gender')
plt.xlabel('Age at enrollment')
plt.ylabel('Average 2nd Semester Grade')
plt.show()


'''
# Find which parental occupations have highest average grades 1st semester
newGroup = students[students["Curricular units 1st sem (approved)"] > 0]
momOcc = newGroup.groupby(["Mother's occupation"])['Curricular units 1st sem (grade)'].mean()
dadOcc = newGroup.groupby(["Father's occupation"])['Curricular units 1st sem (grade)'].mean()
bothOcc = newGroup.groupby(["Father's occupation", "Mother's occupation"])['Curricular units 1st sem (grade)'].mean().reset_index()
#print(dadOcc)
#print(momOcc)
#print(bothOcc)
-----
occupation = newGroup["Father's occupation"].unique()
occupationM = newGroup["Mother's occupation"].unique()
plt.bar(occupationM, momOcc, color='red')
plt.bar(occupation, dadOcc, color='blue')
plt.show()
---------
momOcc.plot(kind='bar', color='red')
plt.ylim(momOcc.min(), momOcc.max())
plt.show()
dadOcc.plot(kind='bar', color='blue')
#plt.bar(momOcc["Mother's occupation"], momOcc['Curricular units 1st sem (grade)'])
'''
