
# coding: utf-8

# In[ ]:


# python_repos.py

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call ans store the response
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'

def get_status_code(url=URL):
    r = requests.get(url)
    return r.status_code
    
    #print("Status code:", r.status_code)

# Store API response in a variable
def get_total_repositories(url=URL):
    r = requests.get(url)
    response_dict = r.json()
    return response_dict['total_count']
    #print("Total repositories:", response_dict['total_count'])

# Explore info about the repositories
def get_top_items_count(url=URL):
    r = requests.get(url)
    response_dict = r.json()
    return len(response_dict['items'])
#     repo_dicts = response_dict['items']
#     print("Number of items:", len(repo_dicts))

# names, plot_dicts = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
    
#     description = repo_dict['description']
#     if not description:
#         description = "No description."
#     plot_dict ={
#         'value': repo_dict['stargazers_count'],
#         'label': description,
#         'xlink':repo_dict['html_url']
#         }
#     plot_dicts.append(plot_dict)
    
# # Make visualization.

# # font size setting in my_style
# my_style = LS('#333366', base_style=LCS)
# my_style.title_font_size = 24
# my_style.label_font_size = 14
# my_style.major_label_font_size = 18

# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.truncate_label = 15 # shorten to 15 characters
# my_config.show_y_guides = False # hide horizontal lines on the graph
# my_config.width = 1000 # set custom width so the chart will use more of the available space in the browser

# chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-starred python projects on github'
# chart.x_labels = names

# chart.add('', plot_dicts)
# chart.render_to_file('python_repos.svg')

