# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:31:01 2022

@author: christian
"""

class Square:
    
    
    def __init__(self):
        
        self.length = 4
        self.width = 4
        
    def set_length(self, l):
        
        self.length = l
        
    def set_width(self, w):
        
        self.width = w
        
    def get_length(self):
        
        return self.length
    
    def get_width(self):
        
        return self.width
    
    
    def compute_area(self):
        
        return self.length * self.length
    
    def compute_perimeter(self):
        
        return 4 * self.length
    
    def print_square(self):
        
        print(f'All sides have a length of {self.length}')
        
    def compare_area(self, other_square):
        
        return self.compute_area() == other_square.compute_area()
    
    def compare_perimeter(self, other_square):
        
        return self.compute_perimeter() == other_square.compute_perimeter()
    