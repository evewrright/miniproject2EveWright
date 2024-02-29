import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("dataset.csv", index_col=0)
'''
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


# Avg grade FIRST SEMESTER by PARENT QUALIFICATION
# Plots a 2 column bar graph with categories being level of parent education
# col1 - at least 1 parent has completed that level.
# col2 - 1 parent has completed that level and the other that level or higher
avgGrades_1sem_1Par = gradeBy1ParentQuals(qualsList, '1st')
avgGrades_1sem_2Par = gradeByBothParentQuals(qualsList, qualsPlusList, '1st')

semester1 = pd.DataFrame({'1 Parent' : avgGrades_1sem_1Par, 'Both Parents' : avgGrades_1sem_2Par}, index=quals)
ax1 = semester1.plot.bar(rot=0)
plt.ylim(11, 13)
plt.ylabel('Mean of 1st Semester Student Grade Averages')
plt.xlabel('Parental Education')
plt.title('Average 1st Semester Grade by Parent Level of Education')
plt.show()

# Avg grade 2ND SEMESTER by PARENT QUALIFICATION
avgGrades_2sem_2Par = gradeByBothParentQuals(qualsList, qualsPlusList, '2nd')
avgGrades_2sem_1Par = gradeBy1ParentQuals(qualsList, '2nd')

semester2 = pd.DataFrame({'1 Parent' : avgGrades_2sem_1Par, 'Both Parents' : avgGrades_2sem_2Par}, index=quals)
ax = semester2.plot.bar(rot=0)
plt.ylim(10, 13.5)
plt.ylabel('Mean of 2nd Semester Student Grade Averages')
plt.xlabel('Parental Education')
plt.title('Average 2nd Semester Grade by Parent Level of Education')
plt.show()

# Avg grade 2ND SEMESTER by AGE AT ENROLLMENT, grouped by GENDER
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

# Units enrolled - approved = unapproved. Average unapproved units by gender
# Get the SettingWithCopyWarning but can't fix it. I tried using .loc in a million ways and still couldn't figure it out
stuEnrolled = students[students["Curricular units 1st sem (enrolled)"] > 0]
stuEnrolled['Units unapproved'] = stuEnrolled['Curricular units 1st sem (enrolled)'] - stuEnrolled['Curricular units 1st sem (approved)']
avgUnapproved = stuEnrolled.groupby(['Gender'])['Units unapproved'].mean()
avgUnapproved.plot.bar()
plt.xlabel('Gender')
plt.ylabel('Average Curricular Units Not Approved')
plt.title('Average Curricular Units Not Approved by Gender')
plt.show()
'''

# Barh
#df2.plot.barh(stacked=True)
#Scholarship holder based on parent qualification
newGroup = students[students["Curricular units 1st sem (approved)"] > 0]

mychart = newGroup.groupby(["Course"])["Gender"].value_counts()
print(mychart)
pivot = pd.pivot_table(data=df, index=['Course'], columns=['Gender'], values='Counts')
mychart.plot.barh(stacked=True);
plt.show()
#for each course how many students are men and how many are women

#agr = newGroup['Course'].value_counts()
#of all students in agronomy, how many have a parent with occupation
#momOcc = newGroup.groupby(["Mother's occupation"])['Scholarship holder'].value_counts()
#dadOcc = newGroup.groupby(["Father's occupation"])["Course"].value_counts()
#counts = newGroup["Mother's occupation"].value_counts()
#dadOcc = newGroup.groupby(["Father's occupation"])['Debtor'].value_counts()


'''
# Credits enrolled 1st semester against inflation rate
#students.plot.scatter(x="GDP", y="Curricular units 1st sem (enrolled)")
#plt.show()

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
'''
# Find Avg 1st Semester Grade by Parent Qualification of BOTH parents
avgGrades_1sem_2Par = gradeByBothParentQuals(qualsList, qualsPlusList, '1st')
plt.bar(quals, avgGrades_1sem_2Par, color='purple')
plt.ylim(min(avgGrades_1sem_2Par) - .5, max(avgGrades_1sem_2Par) + .5)
plt.ylabel('Mean Average Grade of 1st Semester Units')
plt.xlabel("Parental Education of Both Parents")
plt.title("Average of 1st Semester Grades by BOTH Parental Education")
plt.show()
'''
