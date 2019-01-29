# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:17:35 2019

@author: amanda
"""

import sqlite3
import json
import requests
import os


def check_db(db_path):
    if os.path.exists(db_path):
        return True
    else:
        return False
    
    
def get_db():
    conn = sqlite3.connect("phonebook.db")
    c = conn.cursor()
    return c
    
    
#def access_db():
#    get_db().execute("SELECT * FROM person")
#    
#print(access_db())

#def findBusiness(businessName, businessType, location):
    