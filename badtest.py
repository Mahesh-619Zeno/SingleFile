# violations_sample.py

import os,sys   # multiple imports on the same line (PEP8 violation)

def BADFunctionName(x,y): # bad function naming (PEP8 violation)
  if(x==  1):print("x is one") # bad spacing, inline statement
  else:
      print(  "x is not one") # extra spaces
  return(x+y) # bad spacing around operators

def another_func():
    tempList=[1,2,3,4] # no spaces after commas
    for i in range (0,len(tempList)): # space before parenthesis
     print("Value is:",i) # wrong indentation
    return None


class myclass: # class name should be PascalCase
 def __init__(self,name):self.name=name # one-line function definition
 def PrintName(self): # method naming should be snake_case
      print("Name:"+self.name)


unused_var = 42  # unused variable
