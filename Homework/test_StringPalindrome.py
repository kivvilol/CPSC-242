# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 10:24:12 2022

@author: cbweb
"""

from StringPalindrome import StringPalindrome 
    
strpal1 = StringPalindrome('hello')
strpal2 = StringPalindrome('hello')
strpal3 = StringPalindrome('grandview')

print(strpal1.get_first_half())

print(strpal1.compare_palin(strpal2))
print(strpal1.compare_palin(strpal3))

strpal1.set_string_palin('grandview')
print(strpal1.get_string_palin())

