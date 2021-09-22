# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 23:20:03 2021

@author: Barri
"""

# program to run a basic version of the game rock paper and scissors

print('Rock............')
print('Paper...............')
print('Scissors..............')


player1 = input('Player 1, make your move: ')
player2 = input('Player 2, make your move: ')


if player1 == player2:
    print("It's a tie")

elif player1 == 'rock':
    if player2 == 'scissors':
        print("Player1 wins!")
    elif player2 == 'paper':
        print("Player2 wins!")
        
elif player1 == 'paper':
    if player2 == 'rock':
        print('Player1 wins!')
    elif player2 == 'scissors':
        print('Player2 wins')
        
        
elif player1 == 'scissors':
    if player2 == 'paper':
        print('Player1 wins!')
    elif player2 == 'rock':
        print('Player2 wins')
        

    






