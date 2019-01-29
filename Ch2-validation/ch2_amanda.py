# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:12:17 2019

@author: 612436198
"""

#Task 1: Asking user input with a pre-coded new line or a space.
#With a new line:
print("What's your age?")
age = input()
#With a space:
age = input("What's your age? ")
#Remember that user inputs are returned as strings, so may need converting to another type.

#Task 2: Casting str to int.
print("What's your age?")
age = int(input())
#or
age = int(input("What's your age? "))
#or
age = input("What's your age? ")
age_int = int(age)
#Best not to do the last one though, not as efficient.

#Task 3: Casting str to a different case.
option = input("Please input yes or no. ").lower()

#Task 4: An example for validating string length.

userInput = input("Please enter a number three digits long.\n")

while len(userInput) != 3:
    userInput = input("Sorry, please try again. Enter a three digit long number.\n")
print("Thanks!")
    
#Task 5: Using the while True infinite loop.
print("***choice***")
print("1. Display my name.")
print("2. Display my age.")
print("3. Display my city.")

choice = 0

while True:
    choice = int(input("What do you choose? "))    
    while choice < 1 or choice > 3:
        choice = int(input("What do you choose? "))
    break
if choice == 1:
    print("Amanda")
elif choice == 2:
    print("37")
elif choice == 3:
    print("London")

#Task 6: Handling errorful input.
print("***choice***")
print("1. Display my name.")
print("2. Display my age.")
print("3. Display my city.")

choice = 0

while True:
    try:
        while choice < 1 or choice > 3:
            choice = int(input("What do you choose? "))
        break
    except ValueError:
        print("Please type a number!")
if choice == 1:
    print("Amanda")
elif choice == 2:
    print("37")
elif choice == 3:
    print("London")
    
#Task 7: Class-based user input validation.
class Spam(object):
    def __init__(self, description, value):
        if not description or value <= 0:
            raise ValueError
        self.description = description
        self.value = value
#You can also write the code with assert statements (more on those in test driven development):
class Spam(object):
    def __init__(self, description, value):
        assert description != ""
        assert value > 0
        self.description = description
        self.value = value
