# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Task 1: Using 'except'.
try:
    f = open("testfile")
except Exception:
    print("Error!")
#With a more comprehensive error message:
try:
    f = open("testfile")
except Exception:
    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")

#Task 2: Multiple errors, multiple exceptions.
#Because the error in the below is not a file not found error, it does not return the text to be printed for a file not found error. Instead it returns a not defined error.
try:
    f = open("testfile.txt")
    s1 = not_exist
except FileNotFoundError:
    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")
#So you can do:
try:
    f = open("testfile.txt")
    s1 = not_exist
except FileNotFoundError:
    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")
except Exception:
    print("Sorry. Something is wrong after opening function.")
    
#Types of error (there's a library you can check - see curriculum/below):
"""
print(math.sqrt(-1)) is a ValueError.
1 + 2 + "three" is a TypeError.
1 / 0 is a ZeroDivisionError.
for i in range(5) [missing the colon at the end] is a SyntaxError.
"""

#Task 3: Printing out exception as detected.
try:
    f = open("testfile.txt")
    s1 = not_exists
except Exception as e:
    print(e)
#Here e is a variable that represents anything wrong. The system will print the actual error if there is something wrong in the try block.
    
#Task 4: Using the else block.
try:
    f = open("testfile.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
    
#Task 5: Using the finally block.
#With error:
try:
    f = open("testfile")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")
    
#Without error:
try:
    f = open("testfile.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")

#Task 6: Manually raising an exception.
try:
    f = open("testfile.txt")
    if f.name == "testfile.txt":
        raise Exception
except Exception as e:
    print("File names are the same.")
    
"""
NB 'catch-all' exceptions are considered bad practice! Don't use them!
"""

#From Mabel:
"""
Eg of raising a custom exception. Here, I want the file contents to be printed, unless the file specified is 'test.txt' (which in this case, it is).
Full list of errors/exceptions in Python: https://docs.python.org/3/library/exceptions.html
"""
try:
    with open('testfile.txt', 'r') as f:
        f_text = f.read()
    if f.name == 'testfile.txt':
        # it's better to raise specific errors than generic
        raise OSError('that is the wrong file!')
except Exception as e:
    print(e)
else:
    print(f_text)
finally:
    print('this is the end!')