# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:04:21 2019

@author: amand
"""

class Calculator(object):
#    def add(self, x, y):
#        number_types = (int, float, complex)
#        if isinstance(x, number_types) and isinstance(y, number_types):
#            return x + y
#        else:
#            raise ValueError
            
            
    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            import pdb; pdb.set_trace() # new debugging technique
            result = x - y
            print("Result is: {}".format(result))
            return result
        else:
            raise ValueError
            