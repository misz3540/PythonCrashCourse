
# coding: utf-8

# In[1]:


def get_city_country(city, country, population=''):
    """Return a single string of the form 'City, Country'."""
    if population:
        formatted_city_name = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        formatted_city_name = city.title() + ', ' + country.title()
    return formatted_city_name


# In[ ]:




