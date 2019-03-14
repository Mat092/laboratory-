# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:24:40 2019

@author: mattia.ceccarelli3
"""
#%% exercise using numpy

"""
estimate pi using 
"""
import numpy as np
import time

start_time = time.time()

Nshots = 100000
Nexp = 100

x = np.random.uniform(-1,1,(Nshots,Nexp))
y = np.random.uniform(-1,1, (Nshots,Nexp))

res = x**2 + y**2

true_value = res < 1

Nhits = np.sum(true_value, axis = 0)

pies = Nhits/Nshots*4.

pi = np.mean(pies)

run_time = time.time() #time 

time = run_time - start_time


print(pi)
print("Precision computation : ", np.abs(np.mean(pi)-np.pi))
print(time)