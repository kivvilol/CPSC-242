# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:41:20 2022

@author: cbweb
"""

"""
Christian Webster
CPSC-242-A
1/16/2022
Homework 8

"""

### QUESTION A ###
import random

def function1(n):
    
    i = 0 # 1
    
    mlist = [] # 1
    
    for k in range(n): # n
        mlist.append(random.randint(0, 100)) # 1*n
        
    print(mlist)
    while i < n: # n 
        j = n # 1*n
        sum = 0 # 1*n
        while j > 0: # log(n) # 
            
            sum += mlist[(j+i)%n] # 1*log(n)
            
            j = j // 2 # 1*log(n),
            
        print('sum is', sum)
        i += 1 # 1
        
# T(n) =  2log(n) + 4n + 2
# Asymptotic Upper Bound = O(log(n))


### QUESTION B ###

mstring = 'cpsc242' # 1
reverse_string = [] # 1

n = len(mstring) # 1

while n > 0: # n
    
    reverse_string += mstring[n - 1] # 1*n
    n -= 1 # 1*n
    
print(reverse_string)

# T(n) = 2n + 3
# Asymptotic Upper Bound = O(n)
    


### QUESTION C ###



def is_subset(list1, list2):
    
    if len(list1) > len(list2):
        return False

    idx = 0 # 1
    last_idx = len(list2) - 1 # 1
    
    for item in list1: # n
        
        if item == list2[idx]: 
            
            idx += 1 # 1*n
            
            if idx >= last_idx:
                
                return True # 1*n
            
        else:
            
            idx = 0
            
    return False
            


list1 = [1, 2] # 1
list2 = [1, 2, 3] # 1

print(is_subset(list1, list2))

# T(n) = 2n + 4
# Asymptotic Upper Bound = O(n)









    
    
    
    
    
    
    
    
