#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class User():
    
    def __init__(self, first_name, last_name, location, nick_name):
        self.name = first_name.title() + " " + last_name.title()
        self.location = location.title()
        self.nick_name = nick_name.title()
        self.login_attempts = 0
        
    def describe_user(self):
        print("\n" + self.name + " is based in " + self.location + ".")
        print("You can call " + self.name + " " + self.nick_name + ".")
        
    def greet_user(self):
        print("\nHello, " + self.nick_name + "!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
# class Privileges():
    
#     def __init__(self):
#         self.privileges = ['can add post', 'can delete post', 'can ban user']
        
#     def show_privileges(self):
#         print("Administrator has these privileges:")
#         for privilege in self.privileges:
#             print("-" + privilege)

# class Admin(User):
    
#     def __init__(self, first_name, last_name, location, nick_name):
#         super().__init__(first_name, last_name, location, nick_name)
#         self.privileges = Privileges()
        

