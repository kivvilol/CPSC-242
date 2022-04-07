# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:28:31 2022

@author: christian
"""

# function to recursively comput the factorial of some number n
def recursive_factorial(n):
    
    if n == 1: # this is the base case
        
        return 1
    
    else:
        
        return n * recursive_factorial(n - 1) # recursive call
    

n = 3

if n < 0: # needed because factorial cannot be negative, another solution is to multiply n by -1 to make it positive 
    
    print('Number must be positive to compute factorial')
    
elif n == 0: # factorial of 0 is always 1
    
    print(f'{0}! is 1')
    
else:
    
    print(f'{n}! is {recursive_factorial(n)}') # function call
    

'''
STACK FRAME FOR FACTORIAL


recursive_factorial(3) call

    recursive_factorial(2) call
    
        recursive_factorial(1) call (BASE CASE)
        
            returns 1
            
        recursive_factorial(2) = 2 * 1
        
            returns 2
            
    recursive_factorial(3) = 3 * 2
    
        returns 6

'''


def recursive_fibonacci(n):
    
    if n <= 1: # this is the base case
        
        return n
    
    else:
        
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2) # recursive call


n = 4 # n is the number of terms

if n <= 0:
    
    print('Number must be positive to compute fibonacci sequence of n terms')

else:
    
    for i in range(n):
        
        print(recursive_fibonacci(i)) # function call


'''

STACK FRAME FOR FIBONACCI SEQUENCE

recursive_fibonacci(4) call

    recursive_fibonacci(3) call

        recursive_fibonacci(2)
        
            recursive_fibonacci(1) call (BASE CASE)
            
                returns 1
                
            recursive_fibonacci(2) = 1 + recursive_fibonacci(0) = 1
                
                returns 0
                
                returns 1
                
        recursive_fibonacci(3) = 1 + recursive_fibonacci(1) = 2
            
            returns 2
            
    returns in order 0 1 1 2
            
        


                



















