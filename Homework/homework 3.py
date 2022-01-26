# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 07:58:31 2022

@author: christian
"""

"""
Christian Webster
CPSC-242-A
1/28/2022
Homework 3


Expected Inputs:
    
    Question 1
    
    1) We will input numbers from range [10000, 99999]
    2) Check for which numbers are palindromes (same number forward and backward)
    3) If number is a palindrome, sum the digits of the number
    4) Assign the palindrome as each key in a dictionary
    5) Assign the sum of the paladinrome's digits as the value in the dictionary
    6) Output the dictionary containing our palindrome key and sum of palindrome digits value
    
    Question 2
    
    1) Input a list of strings (characters and integers)
    2) Parse list for strings that can be converted to an integer
    3) If an error is not raised, then we know that that string can successfully be converted to an integer, and is also an integer
    4) If error is not raised add it to a new list
    5) Return list with strings that only contain numeric characters
    
"""

# Write code to record all the numbers in the range [10000, 99999] which are Palindromes
# in a dictionary, using the Palindrome number as the key and sum of the digits in the number
# as value. A Palindrome reads the same left to right and right to left. For example, the
# numbers 21312, 88888 are Palindromes. A dictionary entry will look like {21312 : 9,
# 88888 : 40}

# Although this question specifically asks about 5 digit numbers, this will work for any 
# number of digits. 



def palindrome_check(number): # function that checks if the number is a palindrome
    
    mstr = str(number) # converting number to a string so we can index
    
    str_length = len(mstr)
    
    first_digit = 0 # counter starting from the left number (make this number bigger)
    
    last_digit = str_length - 1 # counter starting from the right number (make this number smaller)
    
    is_palindrome = True
    
    while first_digit < last_digit: # this should work for any number of digits, not just 10000-99999
        
        if mstr[first_digit] == mstr[last_digit]: 
            
            first_digit += 1 # incrementing
            
            last_digit -= 1 # incrementing
            
        else:
            
            is_palindrome = False
            
            break
        
    return is_palindrome # returns a boolean that is True if our number is a palindrome

start = 10000 # defining our start value
end = 99999 # defining our end value

palindrome_dict = {}

digit_sum = 0

for num in range(start, end + 1):
    
    if palindrome_check(num) == True:

        for digit in str(num): # sum the digits of our number to assign to value in dictionary
        
            digit_sum += int(digit)
        
        palindrome_dict[num] = digit_sum # assigns our loop number (if it is a palindrome) to the key, and the sum of the loop number's digits as the value
    
        digit_sum = 0 # resetting our sum for every number
    
print(palindrome_dict)
    

    
# Write a function which takes a list of strings as parameter and returns all strings with only 
# numeric characters. For example, Input list = ['hello', 'iowa', '123', 'x123', '34'], return
# from function = ['123', '34']   


# Using try-except to check if an error is raised when converting the string to an integer


def numeric_char_list(mlist):
    
    num_only_list = [] 
    
    for item in range(len(mlist)):
    
        try: # tests converting a str to an integer. if error is not raised, execute what is inside the try block
        
            num_only_list += [str(int(mlist[item]))]     
        
        except ValueError: # lets us skip the value in list if a ValueError is raised 
        
            continue
    
    return num_only_list
    
mlist = ['hello', 'iowa', '123', 'x123', '34']

result = numeric_char_list(mlist)


print(f'Our list with only numeric-character strings is {result}')

































