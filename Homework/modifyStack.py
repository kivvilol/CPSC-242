# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:29:54 2022

@author: christian
"""

class modifyStack:
    
    def __init__(self):
        
        self._items = []
        
    def push(self, item):
        
        self._items.append(item)
        
    def pop(self):
        
        return self._items.pop()
    
    def empty_stack(self):
        
        while self.size() != 0:
            
            self._items.pop()
            
    def top_two_items(self):
        
        a = self._items.pop()
        b = self._items.pop()
        
        return a, b
    
    def is_empty(self):
        
        return not bool(self._items)
    
    def compare_two_stacks(self, other_stack): # comparing two stacks 
        
        is_same = True
        
        if len(self._items) != len(other_stack._items): # checks if length are the same, if not end code and return False
            
            is_same = False
            return is_same
        
        while len(self._items): # checks first item in stack, then pops it
            
            if self._items[0] == other_stack._items[0]:
                
                self._items.pop()
                other_stack._items.pop()
                
            else:
                
                is_same = False
                break
            
        return is_same
    
    def size(self):
        
        return len(self._items)
    
    def size_naive(self): # rewritten size method without len()
        
        sz = 0 # count
        
        while not self.is_empty():
            
            self._items.pop()
            sz += 1 # add 1 to counter every time we pop an item off the stack
            
        return sz
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    