# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:25:18 2022

@author: christian
"""

from Circle import Circle

c1 = Circle()
c1.set_x_y(1, 1)
c1.set_radius(2)
print(f'area is {c1.compute_area()}')

c2 = Circle()
c2.set_x_y(0, 0)
c2.set_radius(2)


print(c1.compare_circle(c2))    

