# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:36:46 2022

@author: christian
"""

from Square import Square

s1 = Square()
s1.set_length(5)
s1.set_width(5)
print(s1.compute_area())
print(s1.compute_perimeter())

s2 = Square()
s2.set_length(4)
s2.set_width(4)


print(s1.compare_area(s2))
print(s1.compare_perimeter(s2))

