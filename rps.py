'''
Program that simulates the game of rock-paper-scissors. User prompted to select an option, computer then randomly selects, compares both choices, determines winner, and prints the winner
'''

from random import randint
from time import sleep

options = ["R", "P", "S"]
LOSS_MESSAGE = "You lost!"
WIN_MESSAGE = "You won!"

def decide_winner(user_choice, computer_choice):
    print "You selected: %s" % user_choice
    print "Computer selecting..."
    sleep(1)
    print "Computer selected %s" % computer_choice
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
        print("It's a tie!")
    elif user_choice_index == 0 and computer_choice_index == 2:
        print(WIN_MESSAGE)
    elif user_choice_index == 1 and computer_choice_index == 0:
        print(WIN_MESSAGE)
    elif user_choice_index == 2 and computer_choice_index == 1:
        print(WIN_MESSAGE)
    elif user_choice_index > 2:
        print("That is invalid!")
        return
    else:
        print(LOSS_MESSAGE)

def play_RPS():
    print("Rock, Paper, or Scissors?")
    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
    sleep(1)
    user_choice.upper()
    computer_choice = options[randint(0, len(options)-1)]
    decide_winner(user_choice, computer_choice)


play_RPS()



    
