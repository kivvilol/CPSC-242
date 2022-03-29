# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:07:32 2022

@author: christian
"""

from Fraction import Fraction

# making an object, object, or instantiation

fraction1 = Fraction() # fraction1 is an Object
fraction1.set_num(1)
fraction1.set_den(5)
fraction1.print_Fraction()

# fraction1.print_Fraction() 

fraction2 = Fraction()
fraction2.set_num(2)
fraction2.set_den(3)
fraction2.print_Fraction()

# fraction1.add_fraction(fraction2)
fraction1.multiply_fraction(fraction2)
fraction1.print_Fraction()