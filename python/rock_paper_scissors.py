from curses.ascii import isdigit
import random

computer_win = 0
user_win = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input(
        "Choose Rock/Paper/Scissor or Q to quit the game: ").lower()

    if user_choice == "q":
        break
    if user_choice not in choices:
        continue

    # generating a random number from 0 to 2 which corresponds to the indexes of 'choices'
    random_number = random.randint(0, 2)

    computer_choice = choices[random_number]
    print("Computer picked", computer_choice + ".")

    if user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        user_win += 1

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        user_win += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        user_win += 1

    elif user_choice == computer_choice:
        print("It's a draw! Try again")

    else:
        print("Compuer wins!")
        computer_win += 1

print("You won", user_win, "times.")
print("The computer won", computer_win, "times.")

print("Game ends!")
