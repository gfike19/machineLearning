import pandas as pd
import numpy as np

studentData = pd.read_excel("C:/Users/aerot/coding/machineLearning/Week3/Assignments/students.xlsx")
studentDf = pd.DataFrame(studentData)
# print("Class 1\n")
# print(studentData[(studentData["class"] == 1)],"\n")
# print("Class 2\n")
# print(studentData[(studentData["class"] == 2)])

# sortByClass = studentDf.sort_values(by="class")
# print(sortByClass)

# TODO Add percentage of all students in separate percentage column
class1 = pd.DataFrame(studentData["class"])
studentData.insert(4, "Class Percent", studentData[studentData(studentData["class"]).c])

# topMathClass1 = pd.DataFrame(studentData[(studentData["class"] == 1)])["maths"]
# print(studentDf["class"] == 1, "\n")
# print(topMathClass1)

