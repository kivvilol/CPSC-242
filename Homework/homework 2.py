# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 23:12:31 2022

@author: christian
"""

"""
Christian Webster
CPSC-242-A
1/16/2022
Homework 2

Code Explanation:
    
    Given some character input sequence, we will count the number of times 
    b, o, b (case insensitive) appear consecutively. The code will end when
    '$' is input. Space is a valid input. 


Sample Inputs/Outputs:
    
    If we input "Hey bob, are you really bob$"
        b, o, b occurs 2 times 
        
    If we input "My name is BoB and my best friend is also bOB$"
        b, o, b occurs 2 times
        
    If we input "bob bob bob bob bob$"
        b, o b occurs 5 times
    

"""

"""

FINAL SOLUTION

Uses a moving window to check if three character inputs are b, o, b
"""

# initializing our three variables 
item1 = '0'
item2 = '0'
char_inp_str = '0'

num_bobs = 0 # initializing number of bobs

sentinel = '$'

char_inp = input('enter your character (sentinel = $): ')

while char_inp != sentinel:
    
    char_inp_str = str(char_inp)
    
    if (item1 == 'b' or item1 == 'B') and (item2 == 'o' or item2 == 'O') and (char_inp_str == 'b' or char_inp_str == 'B'):
        
        num_bobs += 1
       
    # moves the window one position to the right
    item1 = item2
    item2 = char_inp_str
    
    char_inp = input('enter your character (sentinel = $): ')
    
print(f'b, o, b occurs {num_bobs} times')

"""

POSSIBLE SOLUTION 1

Checks if three character inputs in order are b, o b

PROBLEM - sentinel does not work inside the if statements

"""

"""
sentinel = '$' # value that will end our code if input

num_bobs = 0 # count of b, o, b inputs

char_inp = input('enter your character (sentinel = $): ')

while char_inp != sentinel:
    
    if char_inp == 'b' or char_inp == 'B': 
        
        char_inp = input('enter your character (sentinel = $): ')
        
        if char_inp == 'o' or char_inp == 'O':
            
            char_inp = input('enter your character (sentinel = $): ')
            
            if char_inp == 'b' or char_inp == 'B':
                
                num_bobs += 1 # adding 1 to bob count if b, o, b (case insensitive) was input
                
    char_inp = input('enter your character (sentinel = $): ') # if character was not b, continue inputting
    
print(f'b, o, b occurs {num_bobs} times')

"""         
  

"""

POSSIBLE SOLUTION 2

Adds all values into a list and then uses a moving slice to check if three values in order are b, o, b

"""

"""
sentinel = '$'

num_bobs = 0

char_inp = input('enter your character: ')

char_list = []

n = 3

while char_inp != sentinel:
    
    char_list += char_inp
    
    char_inp = input('enter your character: ')

for i in range(len(char_list) - n + 1):
    
    group = char_list[i:i + n]
    
    if (group[0] == 'b' or group[0] == 'B') and (group[1] == 'o' or group[1] == 'O') and (group[2] == 'b' or group[2] == 'B'):
        
        num_bobs += 1
    
print(f'b, o, b occurs {num_bobs} times')

"""






          
