"""
# Project: Rock, Paper, Scissors Game
# Description: This is version 2 which I updated from version 1 when I did updated my programming skills.
A simple Python game where the user plays against the computer. The user chooses between rock, paper,
and scissors, and the computer randomly selects one. The program then determines the winner based on the rules of
the game.
# Level: Intermediate
Author: Pranjal Sarnaik
Date: 2024-11-30
"""

# Importing random module to generate random integer number
import random
from art import rock, paper, scissors, logo
from game_rules import rules

game_images = [rock, paper, scissors]

while True:
    print(logo)
    print(rules)
    print("Welcome to Rock, Paper and Scissors game: Type 0 for Rock, 1 for Paper and 2 for Scissors")

    # Asking uer to choose between 0, 1, 2.
    while True:
        try:
            user_choice = int(input("Please enter your choice (0, 1, 2): "))
            if user_choice in [0, 1, 2]:
                break
            else:
                print("Please enter valid input: (0, 1, 2)")
        except ValueError:
            print("Please enter valid input: (0, 1, 2)")

    if 2 >= user_choice >= 0:
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

    want_to_play = input("Do you want to play again, type 'Y' and 'N': ").upper()

    if want_to_play == "Y":
        print("\n" * 25)
        pass
    else:
        print("See you soon! Stay awesome!!")
        break

    # End of the game
