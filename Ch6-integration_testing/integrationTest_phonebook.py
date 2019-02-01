# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:27:46 2019

@author: amand
"""

from phonebookFunction import *

print("---test check_db---")
print(check_db("phonebook.db"))

print("\n---test get_db---")
print(get_db())

print("\n---test search_type_input---")
print(search_type_input())

print("\n---test business_search_type_input---")
print(business_search_type_input())

print("\n---test business_type_input---")
print(business_type_input())

print("\n---test name_input---")
print(name_input())

print("\n---test postcode_input---")
print(postcode_input())

print("\n---test get_person_data---")
print(get_person_data("Jolly"))

print("\n---test get_businessName_data---")
print(get_businessName_data("Oodoo"))

print("\n---test get_businessType_data---")
print(get_businessType_data("Toys"))

print("\n---test include_location---")
print(include_location())

print("\n---test narrow_by_location---")
print(narrow_by_location(get_person_data("Jolly")))

print("\n---test person_search---")
print(person_search())

print("\n---test businessName_search---")
print(businessName_search())

print("\n---test businessType_search---")
print(businessType_search())

print("\n---test phonebook---")
print(phonebook())