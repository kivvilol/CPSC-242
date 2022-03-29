# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:00:08 2022

@author: christian
"""

# Write a function that takes a 2D Matrix of integers as parameter, and returns the sum of all elements in the matrix. 

"""

def sum_of_2d_list(mlist):
    
    sum_of_elements = 0
    
    for row in mlist:
        
        for col in row:
            
            sum_of_elements += col
            
    return sum_of_elements

twodee_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

print(f'The sum of all numbers in our matrix is {sum_of_2d_list(twodee_list)}')

"""

# Dice game – Player may join the game by depositing an initial payment of $5.00.
# Player rolls 3 dice. If all 3 dice show the number 6, player wins $100 and game
# ends. Each play costs 0.50 cents, game ends when balance reaches 0. Player
# may end the game early and receive the balance left from the initial payment of
# $5.00. Player also receives 0.05 cents times the number on the first dice as
# incentive during each play which is paid out at the end of the game.

import random

# roll_dice
def dice_roll(): # rolling 3 dice and returning them as a tuple
    
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    roll3 = random.randrange(1, 7)
    
    return roll1, roll2, roll3

# check_balance
def check_balance(balance): # checking if there is enough money to play
    
    if balance >= 0.50:
        
        return False

    return True

# game_status
def game_won(dice_tuple): # checking if the player won the game
        
    if dice_tuple[0] == 6 and dice_tuple[1] == 6 and dice_tuple[2] == 6:
        
        return True
    
    return False
    
    
balance = 5.00
ended_early = False
incentive = 0


while not check_balance(balance) or ended_early:
    
    #dice_tuple = dice_roll()
    dice_tuple = (6, 6, 6)
    print(dice_tuple)
    
    if game_won(dice_tuple):
        
        print('You won $100') 
        
        break
    
    # updating the state of the game
    balance -= 0.50
    incentive += dice_tuple[0] * 0.05
    
    print(f'Your current balance is {balance}')
    print(f'Your current incentive is {incentive}')
    
    continue_game = input('Do you want to continue? (y/n): ')
    
    
    if continue_game == 'n':
        
        ended_early = True
    
print(f'Your final balance is {balance}')
print(f'Your final incentive is {incentive}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    

    
    
    























