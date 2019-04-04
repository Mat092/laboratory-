#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:26:50 2019

@author: mattia
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

# values from the numerical recipies
m = 2**32
a = 1664525
c = 1013904223

R0 = 4
R1 = (a*R0+c)%m
R1
    
results = []
for i in range(5000):
    results.append(R1/m)
    R1 = (a*R1+c)%m """not really random number"""
    

plt.hist(results)

#%%
import numpy as np 
import random as rn 
import seaborn as sns

"""
how to generate random number from 

Negative binomial = number of failure before a hit 

it's like a poisson distribution with an average distributed as a gamma function

we can combine distribution to create new type of generations

"""
#%%
import scipy.stats as st 

"""
tons of object to work with distribution, use of dir methods, I don't have dir :(

a cauchy distribution has not defined average.


they don't have a classical parametric classification: described by using a LOCATION and 
a SCALE. ---> Problems and awkward moment, stay allertv of strange arametrizations 
"""

#help(st.gamma.rvs)

"""
RVS = 

"""

#
#data_norm = np.random.randn(1000)
#sns.distplot(data_norm, kde = False, fit = st.norm)

"""
not enough control on the fitting problem, we don't know how it fit the location and other 
parameter 
"""

"""
it guve sus the possibility to give any obj as long as is 
"""
dist1 = st.gamma(2.0, loc=0, scale=1)
dist = st.gamma

class Fitter:
    
    def __init__(self, distribution, **fit_params):
        self.dist = distribution
        self.fit_params = fit_params
        
    def fit(self, data):
        params = self.fit_params
        return self.dist.fit(data, **params)
    
    def pdf(self, x, *params):
        return self.dist.pdf(x, *params)
    
myFitter1 = Fitter(distribution = st.gamma, floc = 0)
myFitter2= Fitter(distribution=st.norm)
    
sns.distplot(dist1.rvs(10_000), kde=False, fit = myFitter1)


#%%





