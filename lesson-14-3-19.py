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
#print("a = ", a)

b = np.array([[1,2,3,4],[5,6,7,8]])
#print("b = ", b)

"""
we can have any dimensions we wnant for our array.
"""
a.shape
a.dtype #array are homogenous (same type of object 
              #inside

a = [1,2,3,4]
a_array = np.array(a)
b_array = np.asarray(list(a))
print(a_array.shape)
print(b_array.shape)
print(a_array.dtype)
print(len(a_array))


"""
different way of creating an array :
    
    zeroes:
        create an array of zeroes of the dimension you need 
    ones :
        create an array of ones of the dimension you need 
    empty :
        in this case, it print zeroes (are almost zeroes).
        But it si a mallock, ou nedd to delete the cells and 
        rewrite it 

the result of an operation is ussually put in a old array,
so you don't waste time and memory 
"""

zero = np.zeros(10)
zero 

empty = np.empty((10,2))

print(empty) 

"""
ranges are anothe rimportant way of creating an arrays 

arange :
    equivalent to range in python 
    
linspace :
     slightly different: starting point and ending point 
     (including them) annd then it specify a number of points 

logspace: 
    expnentially spaced number, not equally spaced as for linspace.
    
geomspace :
    same as logspace, but with number not in log
    
    
Numpy is really rich 
"""

"""
slicing refer to the very number your are viewing: 
    so deleting them, delete the true value in the memory.
"""
#%%
import numpy as np 

# the Sieve of Eratosthenes, numpy version
N = 80
a = np.arange(N)
for i in range(2, N):
    a[i*2::i] = 0 #take a slice of all the multiple of i 

print(a)
print(a[np.nonzero(a)]) #show the prime number 
#%%

"""
Let's see how much faster numpy is:
    it is realy faster, even of th wrong algorithm as before
    
    mean = np.mean(array)
    
    numpy doesn't bother with all the python operations.
"""
import numpy as np 
import time

start_time = time.time() # inizia a contare il tempo
N = int(1e7)
x = np.random.rand(N)
mean_for_1 = 0.0
mean_for_2 = 0.0
for x_i in x:
    mean_for_1 += x_i/N
    mean_for_2 += x_i
mean_for_2 /= N
print ("Mean 1 = {:.32f}".format(mean_for_1))
print ("Mean 2 = {:.32f}".format(mean_for_2))
print ("Calculated in {:.2g} sec".format(time.time()-start_time))

start_time = time.time()
mean_vec = np.mean(x)
print ("Mean from numpy = {:.32f}".format(mean_vec))
print ("Calculated in {:.2g} sec".format(time.time()-start_time))

#%% Other useful things
from numpy import random

"""
a lot of possiilitis even with this library 
can ask for one number only, or arbitrary dimensional arrays.
"""


a = np.array([1, -2, 3.444, -2, 4.29, 6.98])
b = np.array([2, -2, 3.44, -2., 5, 7])

print("\n Some other operations \n")

print(np.abs(a)) # absolute value 
print(np.fabs(a)) # absolute value 
print(np.sqrt(a)) # square root NO Exceptions and error, just warnign???
print(np.floor(a)) # the largest integer value less than or equal to x
print(np.ceil(a)) # smallest integer value greater than or equal to x


"""
pay attention because NAN is contegious.
"""


a = np.array([1, -2, 3.444, -2, 4.29, 6.98])
b = np.array([2, -2, 3.44, -2., 5, 7])

print ("\n SOME ordering operations \n")
print(np.sort(a)) # SORTING ELEMENTS
print(np.argsort(a)) # SORTING INDICES
print(np.where(a < 2)[0]) # INDICES WHERE CONDITION
print(np.where(a > 2, 1, 0)) # (CONDITION, IF(CONDITION), ELSE)
print(np.median(a)) # MEDIAN
print(a[a>0]) # CONDITIONAL SELECTION


#%%Example of images 
from PIL import Image
from IPython.display import display
filename = "./fractal_wrongness.png"

with Image.open(filename) as im:
    print(im.size, im.mode)
    pix = np.array(im)
pix.shape


import pylab as plt
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 12))
ax1.imshow(pix[:,:,0], cmap=plt.cm.Reds)
ax2.imshow(pix[:,:,1], cmap=plt.cm.Greens)
ax3.imshow(pix[:,:,2], cmap=plt.cm.Blues)
ax4.imshow(pix)

#%%Advanced numerical computation 
"""
scikit image is an extension of scipy.ndimage
"""

"""
visualizatin in python is a +wide horizon, matplotlib is the easier and more
versatile 

there are several other that provide more functionality, but they aren't 
interactive 

with matplolib and seaborn you have almost everything 
"""
"""
pylab is a mixture of scipy and matplolib for plotting:
    but the origin of this package is quite recent (as python 15 years)
    before there were only matlab: matplotlib come from matlab and it can 
    have some stuff from it.
"""

import matplotlib.pylab as plt
import numpy as np

data = np.random.randn(1000)

fig, ax = plt.subplots() #create a figure and an axis

"""
whenrver you create a plot: 
    
    figure, its the overall scheme, groups of axes 
    
    axes: fill the all figure 
    
"""
ax.plot(data)

plt.show()

"""
Are they really Gaussian?
"""

data = np.random.randn(1000,2)

fig, ax = plt.subplots()

ax.hist2d(data[:,0], data[:,1], bins = 30)

print()

"""
or a scatter plot 
ax.scatter(x,y)

"""
#%%
"""
for 3d visualization

"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure()
ax = fig.gca(projection='3d')

X, Y = np.mgrid[-3:3:0.05, -3:3:0.05]# creating a bidimensional grid
R = np.sqrt(X**2 + Y**2)
S = np.sinc(R)

surf = ax.plot_surface(X, Y, S, cmap=cm.coolwarm)

#%%

"""
I can also specify how many subplots I want in a figure 

"""


x = np.random.randn(1000) 
y = x**2 + 0.1 + np.random.randn(len(x)) 

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

ax1.scatter(x, y, marker='^')
ax2.hist(x, alpha=0.5, color='r', density=True, bins=33)
ax3.hist(y, label='transformed data', histtype='step')
ax3.legend()
ax3.set_ylabel("$x^2$ value counts")

fig.tight_layout()

#%%Linear Algebra with numpy and scipy 


import numpy as np
import scipy as sp

"""
scipy is more extended in linear algebra overall 
"""


a = np.array([[1,2,3,4,5]])
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

print(np.dot(b, b)) # scalar product of b and b
print(sp.dot(b, b))
print(b@b) #recommended 

"""
tons of linear algebra operations on slides 
"""

#%% Eigenvalue and Eigenvectors 

""""
how to deal with sparse matrices? most method are written for this purpose.

"""

#%%Symbolic algebra 

"""
can be really really useful for physicists, we want to use symbol as a 
mathematical symbol
"""
import sympy

x = sympy.Symbol("x") #Non negative real symbol 
print(x)

y = 1 + x + x**2 # y is a function of x 

"""
tons of utilities:
    limits
    
    derivative 
    
    integrals (definite or indefinitve(really hard))
"""

#%%Differential equations and fitting 

from scipy.integrate import odeint 

"""
integration of the function:
    
    dy/dt = ay
    y(0) = y0
"""
"""
define a function and then use it as a variables:
    
    function are OBJECT, so I can passa function as argument of 
    other functions

"""

def derivative(y,t):
    return -y

time = np.linspace(0, 10, 20)
y0 = 10.0
# integration of the differential equation: (function, initial condition, time)
yt = odeint(derivative, y0, time) 


#plotting, reasonable looking graph 
fig, ax = plt.subplots()

ax.scatter(time, yt, marker = 'o', color = 'k', label = 'exponential')
ax.set_xlabel('time', fontsize = 14) #labels
ax.set_ylabel('y(t)', fontsize = 14)
ax.set_title('Exponential ODEint', fontsize = 16) #title
ax.legend(loc = 'best') #set the legend 

"""
use scatter plot ore a line plot ?


the best graph type is :
    
    what are we trying to show? technically we know onli the points we sample
    scattre should be the correct information
    
    storytelling : lineplot
    
    it dependes on what we are trying to achieve 
"""

y_obs = yt.ravel() + np.random.randn(len(yt))*0.5 #add random noise

fig, ax = plt.subplots()

ax.plot(time, y_obs, 'bo', label = 'sperimentali') #real data 
ax.plot(time, yt, 'k-', label = 'teorici') #theoretical data 
ax.legend(loc = 'best') 

"""
scipy.optimize is a bit too simple, for complex data we need to use
something else
"""






