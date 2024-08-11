'''
SNAKE WATER GUN
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where 
players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, 
the water beats the gun, and the snake beats the water.
Write a python program to create a Snake Water Gun game in python using if-else statements.
Do not create any fancy GUI. Use proper functions to check for win.
'''

import random
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for Water & 2 for Gun : "))


def checkScore(comp, user):
    if(comp == user):
        return 0
    
    if(comp == 0 and user == 1):
        return -1
    
    if(comp == 1 and user == 2):
        return -1
    
    if(comp == 2 and user == 0):
        return -1
    
    return 1

score = checkScore(comp, user)

print("You Choose :", user)
print("Comp Choose :", comp)

if(score == 0):
    print("It's a Draw !!")
elif(score == -1):
    print("You Lose !!")
else:
    print("You Won !!")