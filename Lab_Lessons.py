#%% Exercise Lesson one

#just a comment 

def is_prime(number):
    for num in range(2,number):
        if number % num == 0:
            return False
    return True

def get_primes(max_):
    primes = []
    for num in range(2,max_+1):
        if is_prime(num):
            primes.append(num)
    return primes

get_primes(100)

#another useless comment


#%% Lab Lesson 2 
def inc(x):
    return x+1

assert inc(3) == 4
assert inc(5) == 4
assert inc(6) == 4

#%%
import pytest 

#%% Exercise for today 

import pylab as plt
import numpy as np 

rule30 = {"000": '1',
          "001": '1',
          "010": '1',
          "111": '1',
          "011": '0',
          "100": '0',
          "101": '0',
          "110": '0',
         }

def generate_state():
    return "1111111111111111111111111111111111111111111111110111111111111111111111111111111111111111111111111111"




def evolve(stato):
    new_state = ""
    bounds = stato[-1] + stato + stato[0]
    for i in range(1,len(bounds)-1):
        key = bounds[i-1:i+2]
        new_state = new_state + rule30[key]
    return new_state

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

matrix = simulation(100) #I saved  the data from the simulation
image = [[int(x) for x in i] for i in matrix ] # transforms the data into int, a readable type for imshow 
                 
plt.imshow(image, cmap = "gray") #showcase the image 


######################################################## TEST 

#def test_generation_valid_state():
#    state = generate_state()
#    assert set(state) == {'.', '0'}
#    
#
#def test_generation_single_alive():
#    state = generate_state()
#    num_of_0 = sum(1 for i in state if i=='0')
#    assert num_of_0 == 1
    

    
#%%
import numpy as np

def generate_state_2d():
    stato = np.ones(shape=(100,100))
    stato[50,50] = 0
    return stato

    
def evolve_2d(stato):
    new_state = np.empty(shape = (100,100))
    bounded = np.pad(stato,pad_width = 1,mode = "constant")
    print(len(bounded[1]))
    for i in range(1,len(bounded[1])-1):
        for j in range(len(i)):
            
    
evolve_2d(generate_state_2d())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


