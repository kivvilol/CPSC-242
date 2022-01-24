# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:01:23 2022

@author: christian
"""

"""
Christian Webster
CPSC-242-A
1/18/2022
Classwork - Jan 18

"""

"""

# Calculating y + yy + yyy + yyyy + ... given a single digit y and a number of terms

def sumseries(y, n):
    
    totsum = 0
    
    original_num = y
    
    for i in range(1, n + 1):
        
        totsum += y
        
        y = (y * 10) + original_num
        
    return totsum

y = int(input('enter a number 1-9: '))
n = int(input('enter the number of terms: '))

print(sumseries(y, n))

"""

"""

# Given a string, split the string into a list of tokens at space boundaries
# Example: 'this is cpsc 242 class', mlist = ['this', 'is', 'cpsc', '242', 'class']


def stringsplit(mstr):
    
    splitwords = []
    tempstring = ''
    
    for ch in mstr:
    
        if ch == ' ':
        
            splitwords += [tempstring]
        
            tempstring = ''

        else:
        
            tempstring += ch
            
    splitwords += [tempstring]
        
    return splitwords

mstr = input('enter a string: ')

print(stringsplit(mstr))

"""


mstr = input('enter a string: ')
strlen = len(mstr)

i = 0
buffer = ''

tokenlist = []

while i < strlen:
    
    if mstr[i] == ' ' and mstr[i - 1] != ' ':
           
        tokenlist.append(buffer)
           
        buffer = ''
           
    elif mstr[i] != ' ':
        
        buffer += mstr[i]
        
    i += 1
        
if buffer != '':
    
    tokenlist.append(buffer)
    
print(tokenlist)
       






















