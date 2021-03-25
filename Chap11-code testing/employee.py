
# coding: utf-8

# In[1]:


class EmployeeSalary():
    """Collect employee's name and an updated annual salary."""
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
#         self.raise = 5000
        
    def give_raise(self, raise_amt=5000):
        self.salary += raise_amt
        return self.salary


# In[5]:


# employee1 = EmployeeSalary('Jane', 'Doe', 30000)
# employee1.give_raise(1000)


# In[ ]:




