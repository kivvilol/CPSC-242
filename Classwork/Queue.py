# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:08:10 2022

@author: christian
"""

class Queue:
    
    def __init__(self):
        
        self._items = []
        
    def is_empty(self):
        
        return not bool(self._items)
    
    def enqueue(self, item): # add item into queue
        
        self._items.insert(0, item)
        
    def dequeue(self): # remove item from queue
        
        return self._items.pop()
    
    def size(self):
        
        return len(self._items)
    
    def print_q(self):
        
        print(self._items)
        
