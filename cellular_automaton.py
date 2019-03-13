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
    return ".......0000000000000.........00000000000.............."

def evolve(stato):
    state_with_boundaries = stato[-1] + stato + stato[0] #Circular Bounds Condition
    new_state = ""
    for i in range(1,len(state_with_boundaries)-1):
        key = state_with_boundaries[i-1 : i+2]
        new_char = rule30[key]
        new_state = new_state + new_char
    return new_state

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
    
simul = simulation(100)

import pylab as plt







