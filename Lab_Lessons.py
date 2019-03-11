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

rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }

def generate_state():
    return ".....0......"

def evolve(stato):
    return stato

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

######################################################## TEST 

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
    
    
#%% Logging and debugging 


def myfunc(a,b):
    a = sorted(a)
    b = sorted(b)
    return a[0]>b[0]

myfunc([3,2],[6,5])
    
    
#%%   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


