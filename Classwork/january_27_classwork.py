# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:31:12 2022

@author: christian
"""

class Fraction:
    
    # initialization function
    def __init__(self):
        
        self.num = 0 # numerator
        self.den = 1 # denominator
        
        
    # methods/member functions
    
    # setters
    def set_num(self, input_num):
        
        self.num = input_num
        
    def set_den(self, input_den):
        
        self.den = input_den
        
    def set_num_den(self, input_num, input_den):
        
        self.num = input_num
        
        self.den = input_den
    
    # getters
    def print_Fraction(self):
        
        print(self.num, '/', self.den)
        
    def get_num(self):
        
        return self.num
        
    def get_den(self):
        
        return self.den
    
    def add_fraction(self, other_fraction):
        
        # current fractions numerator = self.num
        # current fractions denominator = self.den
        # other fractions numerator = other_fraction.get_num()
        # other fractions denominator = other_fraction.get_den()
        
        self.num = self.num * other_fraction.get_den() + \
                    self.den * other_fraction.get_num()
                    
        self.den = self.den * other_fraction.get_den()
        
    def multiply_fraction(self, other_fraction):
        
        self.num = self.num * other_fraction.get_num()
        
        self.den = self.den * other_fraction.get_den()
        
        
    
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

        
        
    

