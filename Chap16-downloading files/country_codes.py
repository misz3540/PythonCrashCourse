#!/usr/bin/env python
# coding: utf-8

# In[17]:


from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    different_name_dic = {'ye': 'Yemen, Rep.',
                          'vn': 'Vietnam',
                          've': ['Venezuela, RB','Venezuela'],
                          'va': 'Vatican',
                          'ru': 'Russia',
                          'sy': 'Syria',
                          'sd': 'South Sudan',
                          'tl': 'Timor',
                          'tw': 'Taiwan',
                          'tz': 'Tanzania',
                          'ps': 'Palestine',
                          'ly': 'Libya',
                          'md': 'Moldova',
                          'mk': ['North Macedonia','Macedonia, FYR'],
                          'hk':'Hong Kong SAR, China',
                          'ir': ['Iran, Islamic Rep.', 'Iran'],
                          'kp': ['Korea, Dem. Rep.', 'South Korea'],
                          'kr': 'Korea, Rep.',
                          'la': ['Lao PDR', 'Laos'],
                          'kg':'Kyrgyz Republic',
                          'eg': 'Egypt, Arab Rep.',
                          'do': 'Dominica',
                          'cg': 'Congo, Rep.',
                          'cd': ['Congo, Dem. Rep.', 'Democratic Republic of Congo'],
                          'cz': 'Czechia',
                          'bn': 'Brunei',
                          'bo': 'Bolivia',
                          'mo': 'Macao SAR, China'}
    
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
#         else:
    for code2, name2 in different_name_dic.items():
        if country_name in name2:
            return code2
    # If the country wasn't found, return None
    return None


# In[13]:


# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))


# In[20]:


# print(get_country_code('China'))


# In[ ]:





# In[24]:





# In[ ]:




