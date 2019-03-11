#%% Logging and debugging 

#This code was used to show the basic use of the debugger.

def f1():
    a = 1 
    return a

def f2():
    a = 2
    b = f1()
    return a+b

def f3():
    a = 3
    b = f2()
    return a+b 

f3()


#%%


def myfunc(a,b):
    a = sorted(a)
    b = sorted(b)
    return a[0]>b[0]

myfunc([3,2],[6,5])

#%%



