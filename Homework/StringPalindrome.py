# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:09:41 2022

@author: cbweb
"""

class StringPalindrome:
    
    def __init__(self, mstr):
        
        new_str = ''
        
        for i in range(len(mstr)):
            
            new_str =  mstr[i] + new_str
            
        self.str_palin = mstr + new_str
        
    def set_string_palin(self, nstr):
        
        new_str = ''
        
        for i in range(len(nstr)):
            
            new_str =  nstr[i] + new_str
            
        self.str_palin = nstr + new_str
        
    def get_string_palin(self):
        
        return self.str_palin
    
    def print_string_palin(self):

        print(self.str_palin)
        
    def get_first_half(self):
        
        str_len_half = len(self.str_palin) // 2
        half_str = ''
        
        for i in range(str_len_half):
            
            half_str += (self.str_palin[i])
            
        return half_str
    
    def compare_palin(self, other_palindrome):
        
        if self.get_string_palin() == other_palindrome.get_string_palin():
            
            return True
        
        return False