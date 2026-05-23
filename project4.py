import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "Draw!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
while True:
        player = input("Enter rock, paper, or scissors: ")
        computer = get_computer_choice()
    
        print(f"Computer chose: {computer}")
        print(get_winner(player, computer))

        again = input("Play again? (yes/no): ")
        if again == "no":
            break