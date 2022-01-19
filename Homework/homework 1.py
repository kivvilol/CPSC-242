# -*- coding: utf-8 -"*-
""""
Created on Tue Jan 11 14:52:21 2022

@author: christian
"""""

"""
Christian Webster
CPSC-242-A
1/12/2022
Homework 1

Expected Code Output:
    # 1) If given 8 integers, the highest number entered will be printed.
    # 2) If given a list of floating points of any length, the average of the list will be calculated and printed
    # 3) If given a list of integers (with duplicates), the frequency of each number will be printed in a list of tuples, where each tuple 
    #    includes the original number and its frequency.
"""




# 1) Write code to read 8 integers from input and compute the largest of the 8 numbers

largest_num = 0

for num in range(8):
    
    num_input = int(input('enter an integer: '))
    
    if num_input > largest_num:
        
        largest_num = num_input # replacing largest number each time the new number is larger than the previous

print('The largest number is', largest_num)


# 2) Write a function named compute_average that takes a list of floating-point numbers as a parameter and computes the average. Function must return the average

def compute_average(mlist):
    
    list_len = len(mlist)
    
    sum_list = 0
    
    for num in range(list_len):
        
        sum_list += mlist[num] # adding every number in the list together
        
    average = sum_list / list_len # computing the average of the list
    
    return average
        

        
float_list = [0.1, 1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0]

average_list = compute_average(float_list)

print('The average of our list is', average_list)



# 3) Write a function that takes a list of integers, mlist (may have duplicates), as a parameter and returns a list of tuples such that each tuple  
#    contains an integer in mlist and its frequency.    

def frequency_of_numbers(mlist):
    
    d = {} # empty dictionary
    
    # adding frequency into a dictionary
    for item in mlist:
        
        if item not in d:
            
            d[item] = 1
            
        else:
            
            d[item] += 1
            
    # converting dictionary into a list of tuples
    tuple_list = []
    
    for item in d:

        pair = (item, d[item])
        
        tuple_list += [(pair)]
        
    
    return tuple_list


int_list = [1, 1, 2, 3, 5, 7, 7, 8, 9, 0, 5, 4, 4, 3, 2, 7, 6, 5, 4, 1]

num_and_freq = frequency_of_numbers(int_list)

print(num_and_freq)

