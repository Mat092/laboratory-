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





