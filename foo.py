# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:01:31 2021

@author: jason
"""

def is_divisible_by_k(x,k):
    #Checks whether x is divisible by k    
    if x%k == 0:
        return True

# Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)



x = []
for i in range(0, 1001):
    if (is_divisible_by_k(i,2) or is_divisible_by_k(i, 5) or is_divisible_by_k(i,7) ):
        x.append(i)     
        
print(x)           
#Sum all integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)

sum(x)


