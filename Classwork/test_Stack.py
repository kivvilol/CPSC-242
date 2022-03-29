# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:35:15 2022

@author: christian
"""

from Stack import Stack


getstr = input('enter a string: ')

strstack = Stack()

i = 0

while i < len(getstr):
    
    strstack.push(getstr[i])
    
    i += 1
    
while not strstack.is_empty():
    
    print(strstack.pop(), end = '')
    
print('\n', end = '')