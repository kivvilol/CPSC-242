# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:33:55 2022

@author: christian
"""

def sort_bubble(mlist): # mlist is input

    for i in range(len(mlist)):
        
        for j in range(0, len(mlist) - i - 1):
            
            if mlist[j] > mlist[j + 1]:
                
                mlist[j], mlist[j + 1] = mlist[j + 1], mlist[j]
                
    return mlist

mlist = [35, 12, -5, 4]

print(sort_bubble(mlist))

