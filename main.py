import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

students = pd.read_csv("dataset.csv", index_col=0)

# Function that takes a list of the parent qualifications (quals) by which you are trying to filter and finds all rows
# where either Mother OR Father has one of those qualifications AND where student is enrolled in >0 units 1st sem
def gradeBy1ParentQuals(qualsList, sem):
    avgGrades = []
    for qualif in qualsList:
        filtGroup = students[(students["Mother's qualification"].isin(qualif)) | (students["Father's qualification"].isin(
        qualif)) & (students["Curricular units " + sem + " sem (approved)"] > 0)]
        avgGrade = filtGroup["Curricular units " + sem + " sem (grade)"].mean()
        avgGrades.append(avgGrade)
    return avgGrades

def gradeByBothParentQuals (qualsList, qualsPlusList, sem):
    avgGrades = []
    for i in range(len(qualsList)):
        filtGroup = students[(students["Mother's qualification"].isin(qualsPlusList[i])) & (students["Father's qualification"].isin(
        qualsPlusList[i])) & (students["Mother's qualification"].isin(qualsList[i])) | (students["Father's qualification"].isin(
        qualsList[i])) & (students["Curricular units " + sem + " sem (approved)"] > 0)]
        avgGrade = filtGroup["Curricular units " + sem + " sem (grade)"].mean()
        avgGrades.append(avgGrade)
    return avgGrades

def grade1ByAge(ages):
    filtGroup = students[(students["Age at enrollment"].isin(ages)) & (students["Curricular units 1st sem (approved)"] > 0)]
    avgGrade = filtGroup['Curricular units 1st sem (grade)'].mean()
    return avgGrade

def saveChart(name):
    savefile = 'charts/' + name + '.png'
    plt.savefig(savefile)
    plt.show()

# Variables set up. Highest level of ed COMPLETED (may have done parts of next level of ed)
quals = ['Middle School', 'High School', "Bachelor's", "Master's", "Doctorate"]
MS = [9, 10, 12, 13, 14, 19, 29, 30]
MSPlus = [1, 2, 4, 5, 9, 10, 12, 13, 14, 19, 29, 30]
HS = [1]
HSPlus = [1, 2, 4, 5]
Bach = [2]
BachPlus = [2, 4, 5]
Mast = [4]
MastPlus = [4, 5]
Doc =[5]
qualsList = [MS, HS, Bach, Mast, Doc]
qualsPlusList = [MSPlus, HSPlus, BachPlus, MastPlus, Doc]

# Create charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

# Avg grade FIRST SEMESTER by PARENT QUALIFICATION
# Plots a 2 column bar graph with categories being level of parent education
# col1 - at least 1 parent has completed that level.
# col2 - 1 parent has completed that level and the other that level or higher
avgGrades_1sem_1Par = gradeBy1ParentQuals(qualsList, '1st')
avgGrades_1sem_2Par = gradeByBothParentQuals(qualsList, qualsPlusList, '1st')

semester1 = pd.DataFrame({'1 Parent' : avgGrades_1sem_1Par, 'Both Parents' : avgGrades_1sem_2Par}, index=quals)
ax1 = semester1.plot.bar(color=['#82cbb2', '#08787f'], rot=0)
plt.ylim(11, 13)
plt.ylabel('Mean of Student Average Grade')
plt.xlabel('Parental Education')
plt.title('Average Grade by Parent Level of Education\n1st Semester')
saveChart('1GradeByParQualif')


# Avg grade 2ND SEMESTER by PARENT QUALIFICATION
avgGrades_2sem_2Par = gradeByBothParentQuals(qualsList, qualsPlusList, '2nd')
avgGrades_2sem_1Par = gradeBy1ParentQuals(qualsList, '2nd')

semester2 = pd.DataFrame({'1 Parent' : avgGrades_2sem_1Par, 'Both Parents' : avgGrades_2sem_2Par}, index=quals)
ax = semester2.plot.bar(color=['#dfc5fe', '#8d5eb7'], rot=0)
plt.ylim(10, 13.5)
plt.ylabel('Mean of Student Average Grade')
plt.xlabel('Parental Education')
plt.title('Average Grade by Parent Level of Education\n2nd Semester')
saveChart('2GradeByParQualif')


# Avg grade 2ND SEMESTER by AGE AT ENROLLMENT, grouped by GENDER
filtGroup = students[students["Curricular units 2nd sem (approved)"] > 0]
women = filtGroup[filtGroup['Gender'] == 0]
men = filtGroup[filtGroup['Gender'] == 1]
avgGradeW = women.groupby(['Age at enrollment'])['Curricular units 2nd sem (grade)'].mean()
avgGradeM = men.groupby(['Age at enrollment'])['Curricular units 2nd sem (grade)'].mean()

avgGradeW.plot(color='#0b8b87', label='Women', marker='o')
avgGradeM.plot(color='#ffa756', label='Men', marker='o')
plt.legend(['Women', 'Men'])
plt.xlim(17, 28)
plt.ylim(11.75, 14)
plt.title('Average Grades by Age at Enrollment, Grouped by Gender\n2nd Semester')
plt.xlabel('Age at Enrollment')
plt.ylabel('Mean of Student Average Grade')
saveChart('2GradeByAge')


# Average UNAPPROVED UNITS by GENDER. Units enrolled - units approved = unapproved.
# I keep getting the SettingWithCopyWarning but can't fix it. I tried using .loc in a million ways and still couldn't figure it out
stuEnrolled = students[students["Curricular units 1st sem (enrolled)"] > 0]
stuEnrolled['Units unapproved'] = stuEnrolled['Curricular units 1st sem (enrolled)'] - stuEnrolled['Curricular units 1st sem (approved)']
avgUnapproved = stuEnrolled.groupby(['Gender'])['Units unapproved'].mean()
avgUnapproved.plot.bar(color =['#0b8b87', '#ffa756'])
plt.xticks((0, 1), ('Female', 'Male'), rotation=0)
plt.xlabel('Gender')
plt.ylabel('Average Curricular Units Not Approved')
plt.title('Average Curricular Units Not Approved by Gender\n1st Semester')
saveChart('1UnapprovedByGender')


# COURSE MAKE-UP by GENDER
newGroup = students[students["Curricular units 1st sem (approved)"] > 0]
myChart = newGroup[["Course", "Gender"]].groupby("Course")["Gender"].value_counts().reset_index(name="Count")
pivot = myChart.pivot_table(index='Course', columns='Gender', values='Count', fill_value=0)
ax = pivot.plot.barh(stacked=True, color =['#0b8b87', '#ffa756'])
ax.legend(['Women', 'Men'])
plt.xlabel('Number of Students')
ax.set_title('Gender Distribution in Different Courses', fontsize=16)
saveChart('CourseByGender')


