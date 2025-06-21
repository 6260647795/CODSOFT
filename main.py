'''
 Creating a Rock Paper Scissors Game
'''
import random

def user(rock, paper, scissors):
    print(f"Let's plsy a rock paper scissors game")
    choices = (rock, paper , scissors)

    player_choice = input("Enter a choice({rock}, {psper}, {scissors}: )")
    if player_choice not in choices:
        print("Invalid choice")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer: {computer_choice}, you: {player_choice}")

    if (player_choice == computer_choice):
        print("It's a tie")
    elif(
        (player_choice == rock and computer_choice == paper)or
        (player_choice == paper and computer_choice == scissors)or
        (player_choice == scissors and computer_choice == rock)
    ):
        print("Computer Win!!")
    else:
        print("You loss")
