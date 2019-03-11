#%%

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
    new_state = ""
    for i in range(len(stato))
        triplet = stato[i] + stato[i-1] + stato[i+1]
        char = rule30[triplet]
        new_state = new_state + char
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
    
    
    
evolve("......0......")