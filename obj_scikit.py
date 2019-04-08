#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:22:10 2019

@author: mattia
"""

class ZeroError(ValueError): pass
class NegativeError(ValueError): pass

def myfunction(a):
    if a<0:
        raise NegativeError("the value should not be negative")
    if a==0:
        raise ZeroError("the value should not be zero")
        
    return a*2


myfunction(2)

#%%

"""
we can be very selectvive with what to do with error

this is very used in ontology and acceptancy of object and inheritance.
"""

try:
    myfunction(-1)
except ValueError:
    pass

try :
    myfunction(1)
except ValueError:
    pass

#%%

@Dataclass
class Animal:
    name: str

    def walk(self):
        print(f"{self.name} is walking")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking!")
        
class Snake(Animal):
    def walk(self):
        print(f"{self.name} is slithering!")
        
class Cat(Animal):
    def walk(self):
        super().walk()
        print(f"{self.name} is wagging is tail!")


s = Snake()
d = Dog()
a = Animal()
c = Cat()

a.walk()

d.walk()
d.bark()
s.walk()
c.walk()









