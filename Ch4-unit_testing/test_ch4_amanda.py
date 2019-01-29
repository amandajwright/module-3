# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:27:39 2019

@author: amand
"""

#Task 2: Testing prime functions.

import unittest
from ch4_amanda import check_prime

class PrimesTestCase(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(check_prime(5))

if __name__ == "__main__":
    unittest.main()
    
#Always import the unittest and the functions file that you are going to test with. While using Python's buit-in unit test options, you will also need to use class testUnit with arguments inherited from unittest.TestCase.
    
#Task 4: Adding to test function.
    
class PrimesTestCase(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(check_prime(5))
    def test_is_four_non_prime(self):
        self.assertFalse(check_prime(4).msg="Four is not prime number.")

if __name__ == "__main__":
    unittest.main()
    
#Practice 2

from ch4_amanda import wordcount
import unittest
    
class TestUnit(unittest.TestCase):
    def test_wordcount(self):
        self.assertDictEqual({'foo' : 2, 'bar' : 1}, wordcount('foo bar foo  '))

if __name__ == "__main__":
    unittest.main()        