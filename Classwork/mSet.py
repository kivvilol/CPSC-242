# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:11:49 2022

@author: christian
"""

class mSet:
    
    def __init__(self, mlist):
        
        self.mSetlist = []
        
        # remove duplicates from mlist
        
        self.remove_duplicates(mlist)
        
        
    def remove_duplicates(self, mlist):
        
        for val in mlist:
            
            self.insert_oneitem(val)
        
    def insert_oneitem(self, item):
        
        i = 0
        
        while i < len(self.mSetlist):
            
            if item == self.mSetlist[i]:
                
                break
            
            i = i + 1
            
        if i == len(self.mSetlist):
            
            self.mSetlist.append(item)
            
    def print_set(self):

        print(self.mSetList)
        
