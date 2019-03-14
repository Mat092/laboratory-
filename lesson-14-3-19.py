#%%
print("{:f} = {:.32f}".format(0.1, 0.1)) #scrittura del numero 0.1 con 32 cifre decimali
print("{:.17f} + {:.17f} = {:.17f}".format(0.1, 0.2, 0.1 + 0.2))

print(0.1)

print(0.1 + 0.1 + 0.1 - 0.3)

#%%
a = 0.1
b = 0.2
c = 0.3
print((a + b) + c, a + (b + c))
assert((a + b) + c == a + (b + c)) #verifica della proprietà associativa(+) considerando tutti i bit
#error, the assert is not true 
# we may test if the different betweeen two number is less than somethig 
#%%
import math 

a = 0.5
b = 4.999998

math.isclose(a,b,abs_tol = 0.00003)

#try to guess from your problem if the result is good enough 


#%%

# we can have exact number when we have 1/2^n
#subtractionn is the real deal, if we subtract two numbers that are r
#really close you can have problems

"""
in decimal we have a general precision to represent number 

"""
from decimal import getcontext, Decimal 

getcontext().prec = 6 
Decimal(1)/Decimal(7)

"""
those number are considerably slower than floating points number 
"""

#%%
from fractions import Fraction 

"""
again this is slower than the normal floating point because we need
functions to do this, floating points number are dealt with by the computer
They're are as fast as a computer can be
"""

#%%

"""
floating points can yield exceptions (divide by zero is normal actually)

underflow = trying to represente a number too small, at a certain point 
the result is just zero, period 

overflow = the result is too big to be represented 

Inexact = trying to do an operations tha he can not represent faithfully:
    
    a + b = a     as a and b are different from 0 
    I lost precision. This can actually happens summing very small
    number 
    
"""

"""
The algorithm of course matters
Example of the average.
"""

import random
N = 1000
x = [random.normalvariate(mu=0, sigma=0.1) for i in range(N)]
mean_1 = 0.0
mean_2 = 0.0
for x_i in x:
    mean_1 += x_i / N #sum numbers divide by N  
    mean_2 += x_i # sum all and after divide by N 
mean_2 /= N
print("Media 1 = {:.32g}".format(mean_1))
print("Media 2 = {:.32g}".format(mean_2))
print("difference = {:.4g}".format(mean_2-mean_1))

"""
the difference is not zero.
"""
#%% Cost of operations 

"""
How fast do I do calculations ?
Different operations do take different time to be performed

add and sub : 3 tic

multiplications : 5 tic

divide : 10 times as much 


a famous operation is the square root of a division 
"""

def isqrt(number):
    import numpy as np
    assert number > 0
    threehalfs = 1.5
    x2 = number * 0.5
    y = np.float32(number) #conversione a float32 del numero

    i = y.view(np.int32) #"vedi" y come una variabile int32
    i = np.int32(0x5f3759df) - np.int32(i >> 1) #differenza tra numeri in bit-format
    y = i.view(np.float32)

    y = y * (threehalfs - (x2 * y * y))
    return float(y)

%timeit isqrt(4)


def func(number):
    return 1/(math.sqrt(number))

%timeit func(4) # this is reeeeally slow compared to the above one

#%% Speed 

"""
there is parallelization
memory acces optimizations

Vectorizations is really important : 
    
    NUMPY 

 do the same operations on evry element of an array.

Vectorization when:
    
    -loop over data ìstructure 
    -can execute the same operation in parallel 
 
a numpy array support vectorized parallel computation:
    
    code in numpy is easier to read 
    numpy is actually C, not python, very highly optimized C functions
    
    keras and tensorflow use the same trick for neural network 
"""
import numpy as np 

a = np.array([1,2,3,4])
print("a = ", a)

b = np.array([[1,2,3,4],[5,6,7,8]])
print("b = ", b)

"""
we can have any dimensions we wnant for our array.
"""
#%%





















