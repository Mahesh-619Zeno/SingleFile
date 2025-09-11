"""This is a program to check if a number is prime or not"""
import os

number = 29
flag = False

api_key = os.getenv("gemini_api")

if number == 0 or number == 1:
    print(number, "is not a prime number")
elif number > 1:
    # check for factors
    for i in range(2, number):
        if (number % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flage:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")

