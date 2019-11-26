import pandas as pd
import numpy as np

studentData = pd.read_excel("C:/Users/aerot/coding/machineLearning/Week3/Assignments/students.xlsx")
studentDf = pd.DataFrame(studentData)

# Filter class 1 and class 2 students - COMPLETE
# print("Class 1\n")
# print(studentData[(studentData["class"] == 1)],"\n")
# print("Class 2\n")
# print(studentData[(studentData["class"] == 2)])
# sortByClass = studentDf.sort_values(by="class")
# print(sortByClass)

# TODO Add percentage of all students in separate percentage column
# class1 = pd.DataFrame(studentData["class"])
# studentData.insert(4, "Class Percent", )

# Topper of class 1 in math - COMPLETE
# topMathClass1 = pd.DataFrame(studentData[(studentData["class"] == 1)])["maths"]
# print(studentDf["class"] == 1, "\n")
# print(topMathClass1.head())

# Topper of class 2 in english -COMPLETE
# topEngClass2 = pd.DataFrame(studentData[(studentData["class"] == 2)])["english"]
# print(studentDf["class"] == 2, "\n")
# print(topEngClass2.head())

# Topper in both classes - COMPLETE ?
# print(studentData.head())

# TODO Names of the students which starts with ‘A’ along with their class
# namesStartA = pd.DataFrame(studentData[studentData["Name"]]).apply(startsWith("A"))
# print(namesStartA)

# Names of all students who failed in class 1 in any subject (less than 40% mark is a fail in any subject) COMPLETE ?
# class1F = studentData[(studentData["class"] == 1) & ((studentData["maths"] < 40) | (studentData["science"] < 40) | (studentData["english"] < 40))]
# print(class1F)

# Names of students in class 1 who failed in all subjects - COMPLETE ?
# class1F = studentData[(studentData["class"] == 1) & (studentData["maths"] < 40) & (studentData["science"] < 40) & (studentData["english"] < 40)]
# print(class1F)
