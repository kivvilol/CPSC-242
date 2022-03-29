# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:30:07 2022

@author: christian
"""

"""

def mod_str(mstr):
    
    new_str = ''
    
    for char in range(len(mstr)):
        
        if mstr[char] == 'h' or mstr[char] == 'k' or mstr[char] == 'p':
            
            new_str += mstr[char]
            new_str += '#'
            
        else:
            
            new_str += mstr[char]
            
    return new_str
    
    
    
mstr = 'hiskid'

print(mod_str(mstr))

"""

"""

class Address:
    
    def __init__(self):
        
        self.homenumber = 1234
        self.streetname = 'Grandview'
        self.lastpart = 'Ave'
        
    def get_address(self):
        
        return str(self.homenumber) + self.streetname + self.lastpart
    
    def set_address(self, num, street, lastpart):
        
        self.homenumber = str(num)
        self.streetname = street
        self.lastpart = lastpart
    
    def compare_address(self, other_address):
        
        if self.get_address() == other_address.get_address():
            
            return True
        
        return False
    
address1 = Address()
address2 = Address()

address1.set_address(15144, 'Iowa', 'Street')
print(address1.get_address())

print(address2.get_address())
print(address1.compare_address(address2))

address2.set_address(15144, 'Iowa', 'Street')
print(address1.compare_address(address2))
    
"""



def int_has_789(minput):
    
    str_input = str(minput)
    
    i = 0
    
    has_seven = False
    has_eight = False
    has_nine = False
    
    while i < len(str_input):
        
        if str_input[i] == '7':
            
            has_seven = True
            
        elif str_input[i] == '8':
            
            has_eight = True
            
        elif str_input[i] == '9':
            
            has_nine = True
            
        i += 1
    
    if has_seven and has_eight and has_nine:
        
        return True
    
    return False


minput = input('Enter an integer: ')
    
    
print(int_has_789(minput))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    