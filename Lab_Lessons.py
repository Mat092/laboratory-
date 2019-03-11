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
    return "11111111110111111111"

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

matrix = simulation(50)

image = [int(x) for i in matrix 
                 for x in i]

image

import pylab as plt

plt.imshow(image)



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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


