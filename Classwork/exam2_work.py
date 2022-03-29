# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:56:33 2022

@author: christian
"""

def three_or_more_vowels(mlist):
    
    new_list = []
    
    for word in mlist:
        
        vowel_count = 0
        
        for letter in word:
            
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                
                vowel_count += 1
                
        if vowel_count >= 3:
            
            new_list += [word]
            
    return new_list

            
 
mlist = ['apple', 'bingus', 'joe', 'orange', 'peanut']

print(three_or_more_vowels(mlist))