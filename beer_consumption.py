# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:36:41 2019

@author: mattia.ceccarelli3
"""


import pandas as pd
import numpy as np
import seaborn as sns

nobel_url = "https://www.britannica.com/topic/Nobel-Prize-Winners-by-Year-1856946"
beer_url = "https://en.wikipedia.org/wiki/List_of_countries_by_beer_consumption_per_capita"

nobelSet = pd.read_html(nobel_url,)[0]
beerSet = pd.read_html(beer_url,)[0]


#%%

selection = nobelSet["category"]=="physics"

physics = nobelSet[selection]

#%%

del physics["name"]
del physics["year"]
del physics["achievement"]
del physics["literary area"]

#%%

nobel = pd.pivot_table(physics,
                       index = "country*",
                       columns = "category",
                       aggfunc = pd.Series.count,

        )

#%%
