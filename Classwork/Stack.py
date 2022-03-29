# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:19:11 2022

@author: christian
"""

class Stack:
    
    def __init__(self):
        
        self._items = []
        
    def push(self, item):
        
        self._items.append(item)
        
    def pop(self):
        
        return self._items.pop()
    
    def is_empty(self):
        
        return not bool(self._items)
    
    def size(self):
        
        return len(self._items)