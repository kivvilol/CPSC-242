# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:32:24 2022

@author: christian
"""

"""

Christian Webster
CPSC-242-A
2/04/2022
Homework 4

"""

class Quadrilateral:
    
    # initialization
    
    def __init__(self):
        
        self.point1 = [0, 0]
        self.point2 = [0, 1]
        self.point3 = [1, 0]
        self.point4 = [1, 1]
        
        
        
    # getters
    
    def get_x(self, point): # defaults to returning point1 if value is out of range
        
        if point == 6:
            
            return self.point6[0]
    
        elif point == 5:
            
            return self.point5[0]
    
        elif point == 4:
            
            return self.point4[0]
        
        elif point == 3:
            
            return self.point3[0]
        
        elif point == 2:
            
            return self.point2[0]
        
        else:
            
            return self.point1[0]
        
        
    def get_y(self, point): # defaults to returning point1 if value is out of range
        
        if point == 6:
        
            return self.point6[1]

        elif point == 5:
        
            return self.point5[1]
    
        elif point == 4:
            
            return self.point4[1]
        
        elif point == 3:
            
            return self.point3[1]
        
        elif point == 2:
            
            return self.point2[1]
        
        else:
            
            return self.point1[1]
        
        
    def get_coord(self, point): # defaults to returning point1 if value is out of range
        
        if point == 6:
            
            return self.point6
        
        elif point == 5:
            
            return self.point5
    
        elif point == 4:
            
            return self.point4
        
        elif point == 3:
            
            return self.point3
        
        elif point == 2:
            
            return self.point2
        
        else:
            
            return self.point1
        
    
    def print_quad(self):

            print(self.point1, self.point2, self.point3, self.point4)

    
    # setters
    
    def set_x(self, new_x, point): # defaults to returning point1 if value is out of range
    
        if point == 6:
            
            self.point6[0] = new_x
            
        elif point == 5:
            
            self.point5[0] = new_x
        
        elif point == 4:
            
            self.point4[0] = new_x
        
        elif point == 3:
            
            self.point3[0] = new_x
        
        elif point == 2:
            
            self.point2[0] = new_x
        
        else:
            
            self.point1[0] = new_x
        
        
    def set_y(self, new_y, point): # defaults to setting point1 if value is out of range
    
        if point == 6:
            
            self.point6[1] = new_y
            
        elif point == 5:
            
            self.point5[1] = new_y    
        
        elif point == 4:
            
            self.point4[1] = new_y
        
        elif point == 3:
            
            self.point3[1] = new_y
        
        elif point == 2:
            
            self.point2[1] = new_y
        
        else:
            
            self.point1[1] = new_y
        
        
    def set_coord(self, new_x, new_y, point): # defaults to setting point1 if value is out of range
    
        if point == 6:
            
            self.point6[0] = new_x
            self.point6[1] = new_y
        
        elif point == 5:
            
            self.point5[0] = new_x
            self.point5[1] = new_y
            
        elif point == 4:
            
            self.point4[0] = new_x
            self.point4[1] = new_y
        
        elif point == 3:
            
            self.point3[0] = new_x
            self.point3[1] = new_y
        
        elif point == 2:
            
            self.point2[0] = new_x
            self.point2[1] = new_y
        
        else:
            
            self.point1[0] = new_x
            self.point1[1] = new_y
        
        
    # methods
    
    def distance(self, first_point, second_point): # distance between two point (length of a side)
        
        x1 = self.get_x(first_point)
        x2 = self.get_x(second_point)
        
        y1 = self.get_y(first_point)
        y2 = self.get_y(second_point)
        
        d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        
        return d
    
    def quad_perimeter(self): # sum of length of sides (perimeter)
        
        side1 = self.distance(1, 2)
        side2 = self.distance(2, 3)
        side3 = self.distance(3, 4)
        side4 = self.distance(4, 1)
        
        total = side1 + side2 + side3 + side4
        
        return total
        
        
        
       
    
class Pentagon(Quadrilateral): # pentagon class that inherits the methods of our quadrilateral

    def __init__(self):
        
        self.point1 = [2, 0]
        self.point2 = [6, 0]
        self.point3 = [7, 4]
        self.point4 = [2, 7]
        self.point5 = [0, 4]
        
    def pent_perimeter(self):
        
        side1 = self.distance(1, 2)
        side2 = self.distance(2, 3)
        side3 = self.distance(3, 4)
        side4 = self.distance(4, 5)
        side5 = self.distance(5, 1)
                
        total = side1 + side2 + side3 + side4 + side5
        
        return total
        
    def print_pent(self):

            print(self.point1, self.point2, self.point3, self.point4, self.point5)
    
class Hexagon(Quadrilateral): # hexagon class the inherits the methods of our quadrilateral
    
    def __init__(self): 
    
        self.point1 = [0, 0]
        self.point2 = [2, 1]
        self.point3 = [2, 3]
        self.point4 = [0, 5]
        self.point5 = [-2, 3]
        self.point6 = [-2, 1]
        
    def hex_perimeter(self): # sum of length of sides (perimeter)
        
        side1 = self.distance(1, 2)
        side2 = self.distance(2, 3)
        side3 = self.distance(3, 4)
        side4 = self.distance(4, 5)
        side5 = self.distance(5, 6)
        side6 = self.distance(6, 1)
        
        total = side1 + side2 + side3 + side4 + side5 + side6
        
        return total
    
    def print_hex(self): # printing the hexagon points

            print(self.point1, self.point2, self.point3, self.point4, self.point5, self.point6)
        
