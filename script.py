# Load libraries
import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data

# Print summary statistics for all columns

# Calculate mean

# Calculate median

# Calculate mode

# Calculate range

# Calculate standard deviation

# Calculate MAD

# Create a histogram of math grades


plt.show()
plt.clf()

# Create a box plot of math grades


plt.show()
plt.clf()

# Calculate number of students with mothers in each job category

# Calculate proportion of students with mothers in each job category

# Create bar chart of Mjob


plt.show()
plt.clf()

# Create pie chart of Mjob


plt.show()

print(students.head())


print(students.describe(include='all'))

mean_math_grade = students['math_grade'].mean()
print(mean_math_grade)


median_math_grade = students['math_grade'].median()
print(median_math_grade)

mode_math_grade = students['math_grade'].mode()[0]
print(mode_math_grade)

range_math_grade = students['math_grade'].max() - students['math_grade'].min()
print(range_math_grade)

std_math_grade = students['math_grade'].std()
print(std_math_grade)

mad_math_grade = students['math_grade'].mad()
print(mad_math_grade)

plt.show()
plt.clf()


sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()


mjob_counts = students['Mjob'].value_counts()
print(mjob_counts)

mjob_proportions = students['Mjob'].value_counts(normalize=True)
print(mjob_proportions)


sns.countplot(x='Mjob', data=students)
plt.show()
plt.clf()


students['Mjob'].value_counts().plot.pie(autopct='%1.1f%%')
plt.ylabel('')  # Optional: to remove the y-label
plt.show()
