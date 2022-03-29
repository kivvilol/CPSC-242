# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:14:08 2022

@author: christian
"""

class Circle:
    
    def __init__(self):
        
        self.x1 = 0
        self.y1 = 0
        self.radius = 0
        
    def set_x_y(self, xc, yc):
        
        self.x1 = xc
        self.y1 = yc
        
    def set_radius(self, rad):
        
        self.radius = rad
        
    def get_center(self):
        
        return self.x1, self.y1
    
    def get_radius(self):
        
        return self.radius
        
    def compute_area(self):
        
        return 3.14 * self.radius * self.radius
    
    def compute_perimeter(self):
        
        return 2 * 3.14 * self.radius
    
    def print_circle(self):
        
        print(self.x1, self.y1, self.radius)
        
    def compare_circle(self, other_circle):
        
        return self.compute_area() == other_circle.compute_area()