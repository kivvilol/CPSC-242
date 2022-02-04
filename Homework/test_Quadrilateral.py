# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 08:59:02 2022

@author: christian
"""

from Quadrilateral import Quadrilateral
from Quadrilateral import Pentagon
from Quadrilateral import Hexagon

quad1 = Quadrilateral()

pent1 = Pentagon()

hex1 = Hexagon()

# testing setters
quad1.set_coord(4, 5, 3)
pent1.set_coord(3, 1, 5)
hex1.set_coord(2, 8, 6)

# testing getters
print(quad1.get_coord(3))
print(pent1.get_coord(5))
print(hex1.get_coord(6))

# testing distance method
print(quad1.distance(1, 4))
print(pent1.distance(3, 5))
print(hex1.distance(2, 6))

# testing print methods
quad1.print_quad()
pent1.print_pent()
hex1.print_hex()    

# testing sum of lengths (perimeter) of all sides
print(quad1.quad_perimeter())
print(pent1.pent_perimeter())
print(hex1.hex_perimeter())




