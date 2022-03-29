# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:09:37 2022

@author: christian
"""

def find_largest_num(mlist, maxrange):
    
    largest_num = 0
    n = len(mlist)
    
    i = 0
    index = 0
    
    for val in mlist[0:n-maxrange]:
        
        if largest_num <= val:
            
            largest_num = val
            index = i
            
        i += 1
            
    return index, largest_num


def selection_sort(mlist):
    
    n = len(mlist)
    
    for i in range(n-1):
        
        index, largest_num = find_largest_num(mlist, i)
        
        print(index, largest_num)
    
        mlist[n - 1 - i], mlist[index] = mlist[index], mlist[n - 1 - i]
    
        print(mlist)
    
    
    
selection_sort([12, 3, 0, 6, 45, -5])
    