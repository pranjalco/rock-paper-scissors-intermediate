"""
# Project: Rock, Paper, Scissors Game
# Description: A simple Python game where the user plays against the computer. The user chooses between rock, paper,
and scissors, and the computer randomly selects one. The program then determines the winner based on the rules of
the game.
# Level: Beginner
Author: Pranjal Sarnaik
Date: Not Remembered
"""

# Importing random module to generate random integer number
import random

# Here we are defining ascii art code for Rock, Paper and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
print("Welcome to Rock, Paper and Scissors game: Type 0 for Rock, 1 for Paper and 2 for Scissors")

# Asking uer to choose between 0, 1, 2.
user_choice = int(input("Please enter your choice (0, 1, 2): "))

if user_choice <= 2 and user_choice >= 0:
    print(game_images[user_choice])

# Computer choosing random number using random module
computer_choice = random.randint(0,2)
print(f"Computer choose:\n{game_images[computer_choice]}")

# Checking the conditions for win and loose by comparing choice of user and computer
if user_choice == computer_choice:
    print("It is draw")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You Win!")
else:
    print("You Loose")

# End of the game




