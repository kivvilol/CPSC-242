# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:02:58 2022

@author: christian
"""

"""
Christian Webster
CPSC-242-A
1/13/2022
"""

# given a list and a key, write code to determine if key is in the list

def check_key(mlist, key):
        
    return key in mlist # returns a boolean with less code than return True 
    
key = 'a'

mlist = ['a', 'b', 'c', 'd', 'e']

print(check_key(mlist, key))


def check_key_v2(mlist, key):
    
    for val in mlist:
        
        if val == key: # 1 timeunit
            
            return True
        
    return False
       
key = 'a'

mlist = ['a', 'b', 'c', 'd', 'e']

print(check_key_v2(mlist, key))




N = 10
i = 0 # counter

while i < N: # loop condition

    print(i) # loop body
    
    i += 1   # iteration count
    

while True:
    
    # set up a condition to terminate the loop
    n = input('n: ')
    
    if n == 'stop':
        
        break
    
    print(n)
    
    
    
    
    