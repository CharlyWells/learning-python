#!/usr/bin/env python3
#using copy() function
import copy
spam = ['A','B','C','D']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese))
cheese[1] = 42
print(spam)
print(cheese)
