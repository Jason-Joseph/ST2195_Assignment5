# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:39:25 2021

@author: jason
"""
def is_divisible_by_k(x,k):
    '''
    Checks whether x is divisible by k.
    '''
    try:
       assert x%k == 0 
       return True
    except AssertionError:
        if k == 2:
            print(f"{x} is not divisible by 2")
        elif k == 5:
             print(f"{x} is not divisible by 5")
        elif k == 7: 
            print(f"{x} is not divisible by 7")
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''

x = []
for i in range(10):
    if is_divisible_by_k(i,2) == True or is_divisible_by_k(i,5) == True or is_divisible_by_k(i,7) == True:
        x.append(i)

print(x)
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
'''

sum(x)