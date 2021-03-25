#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""A class that can be used to represent restaurants.
"""
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nWelcome to " + self.name.title() + "!")
        print("We serve " + self.type.title() + " cuisine.")
        
    def open_restaurant(self):
        print("We are now open!")
        
    def set_number_served(self, number_of_diners):
        self.number_served = number_of_diners
        
    def increment_number_served(self, daily_no_of_customers):
        self.number_served += daily_no_of_customers

