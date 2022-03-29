# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:58:47 2022

@author: christian
"""

"""
Christian Webster
CPSC-242-A
1/18/2022
Classwork - Jan 18

"""

# function that calculates that factorial of n incrementally

"""
def factorial(n):

    fact = 1
    
    for num in range(2, n + 1):
        
        fact = fact * num
        
    return fact

number = int(input('enter a number: '))

print(f'{number}! is {factorial(number)}')

"""

# function that calculates the factorial of n decrementally

"""
def factorial_v2(n):

    fact = 1
    
    while n > 0: # while loop because we don't know the number of iterations
        
        fact = fact * n
        
        n -= 1
        
    return fact

number = int(input('enter a number: '))

print(f'{number}! is {factorial_v2(number)}')

"""

"""

def factorial_v3(n):
    
    fact = n
    
    for i in range(1, n):
        
        fact = fact * (n - i)
        
    return fact

number = int(input('enter a number: '))

print(f'{number}! is {factorial_v3(number)}')

"""

# Dictionary Problem

"""

def square_dict(start, end):
    
    mdict = {}
    
    for i in range(start, end + 1):
        
        mdict[i] = i * i
        
    return mdict

def lookup_value(lookuptable, key):
    
    return lookuptable[key]

key = int(input('enter the key: '))

print(f'The value for {key} is {lookup_value(square_dict(1, 20), key)}')

"""

# Checking all numbers between 500 and 999 for numbers where every digit is even

"""

def all_even(n):
    
    while n != 0:
        
        digit = n % 10
        
        if digit % 2 != 0:
            
            return False
        
        n = n // 10  # removing right digit
        
    return True # if no digit is odd


start = 500
end = 999

for number in range(start, end + 1):
    
    if all_even(number):
        
        print(number)

"""

    





        























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    