#!/usr/bin/python3

update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }

#Updating a dictionary by replasing
#value C with python

new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("__")
print_sorted_dictionary(a_dictionary)

#Adding new key_value_pair to
#an existing dictionary

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("__")
print_sorted_dictionary(a_dictionary)
