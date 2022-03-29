# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:55:02 2022

@author: christian
"""

class IntList:
    
    def __init__(self, Listofints): # Listofints need not be in sorted order
    
        self.mlist = [] # hold integers in always sorted order
        
        for val in Listofints:
            
            i = 0
            
            if not self.mlist:
                
                self.mlist.append(val)
                
            else:
                    
                if val <= self.mlist[0]:
                        
                    self.mlist.insert(0, val)
                
                else:
                    
                    while i < len(self.mlist):
                        
                        if val >= self.mlist[i] and val < self.mlist[i + 1]:
                            
                            self.mlist.insert(i + 1, val)
                            
                            break
                            
                
        
        
    def print_list(self):
        
        print(self.mlist)
        

    
        
        