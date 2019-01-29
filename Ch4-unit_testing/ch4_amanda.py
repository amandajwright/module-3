# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:27:05 2019

@author: amand
"""

#Task 1: Checking for prime numbers.

def check_prime(number):
    """Return True if *number* is prime."""
    for num in range(number):
        if number % num == 0:
            return False
    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if check_prime(index):
            print(index)
            
#Task 3: Final version of prime number function.

def check_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False 
    for num in range(2, number):
        if number % num == 0:
            return False 
    return True

#Practice 2
    
def wordcount(text_body):
    words = text_body.split()
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result