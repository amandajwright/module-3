# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:22:06 2019

@author: amand
"""

import sqlite3
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

def person_search(name, postcode):
    persons = get_person_data(name)
    if len(persons) == 0:
        return "Sorry, your search produced no results."
    else:
        if postcode != None:
            persons = narrow_by_location(persons, postcode)
            if len(persons) == 0:
                return "Sorry, your search produced no results."
            else:
                return persons
        else:
            return persons

def business_name_search(business_name, postcode):
    businesses = get_businessName_data(business_name)
    if len(businesses) == 0:
        return "Sorry, your search produced no results."
    else:
        if postcode != None:
            businesses = narrow_by_location(businesses, postcode)
            if len(businesses) == 0:
                return "Sorry, your search produced no results."
            else:
                return businesses
        else:
            return businesses

def business_type_search(business_type, postcode):
    businesses = get_businessType_data(business_type)
    if len(businesses) == 0:
        return "Sorry, your search produced no results."
    else:
        if postcode != None:
            businesses = narrow_by_location(businesses, postcode)
            if len(businesses) == 0:
                return "Sorry, your search produced no results."
            else:
                return businesses
        else:
            return businesses

def get_person_data(person):
    c = get_db()
    c.execute("SELECT * FROM person WHERE surname = ?", (person,))
    return c.fetchall()

def get_businessName_data(businessName):
    c = get_db()
    c.execute("SELECT * FROM business WHERE business_name = ?", (businessName,))
    return c.fetchall()

def get_businessType_data(businessType):
    c = get_db()
    c.execute("SELECT * FROM business WHERE business_category = ?", (businessType,))
    return c.fetchall()

def narrow_by_location(results_list, postcode):
        results = []
        for deets in results_list:
            if postcode in deets:
                results.append(deets)
            else:
                results = results
        return results
