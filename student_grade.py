# student_grades.py

import json,sys   # multiple imports on same line (PEP8 violation)

def CalculateGrade(marks):   # function name not snake_case
  if marks>90: return "A+"   # one-liner return (bad readability)
  elif marks>75:return "A"
  elif marks>60: return "B"
  elif marks>40:return "C"
  else: return "F"

class student:   # class name not PascalCase
 def __init__(self,Name,Age,Marks):  # parameters not snake_case
    self.Name=Name   # inconsistent attribute naming
    self.age=Age
    self.MARKS=Marks

 def getDetails(self):   # method name not snake_case
        return "Student: " + self.Name + ", Age: " + str(self.age) + ", Grade: " + CalculateGrade(self.MARKS)  # string concatenation instead of f-string

def SaveDataToFile(students,filename="students.json"):  # bad function name, spacing
    with open(filename,"w") as f:
        json.dump([s.__dict__ for s in students],f,indent=4)

if __name__=="__main__":  # spacing violation
    students=[]
    students.append(student("Alice",20,92))
    students.append(student("bob",19,67)) # inconsistent naming
    students.append(student("Charlie",21,45))
    for s in students: print(s.getDetails())  # loop and print on one line
    SaveDataToFile(students,"student_data.json")
