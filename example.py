# bad_example2.py

import sys,os   # multiple imports on one line (not PEP8)
import math     # unused import

def addNumbers(a,b):   # function name not snake_case, missing docstring
  return  a+  b  # inconsistent spacing

def multiply_numbers(x,y,z =2): # space around = is wrong
    result=x*y*z
    return  result  

class myclass:   # class name not PascalCase
   def __init__(self,Value):  # param name not snake_case
      self.Value=Value   # inconsistent attribute naming

   def printvalue(self):  # method name not snake_case
        print("The Value is: " + str(self.Value))  # string concatenation instead of f-string

def very_long_function_name_with_too_many_parameters(param1,param2,param3,param4,param5,param6,param7,param8,param9):
    # Line too long, bad formatting
    return param1+param2+param3+param4+param5+param6+param7+param8+param9

if __name__=="__main__":
    print(addNumbers( 5 ,3 ))  # extra spaces inside parentheses
    obj=myclass(10)
    obj.printvalue()
    print(multiply_numbers(2,3))
