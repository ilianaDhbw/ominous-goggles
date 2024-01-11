import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}." + "\033[33m" +  "It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Scissors cuts paper!"+"\033[35m" + "You win!")
    else:
        print("Paper covers rock!"+ "\033[36m" + "You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Scissors cuts paper!"+"\033[35m" + "You win!")
    else:
        print("Paper covers rock!"+ "\033[36m" + "You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper!"+"\033[35m" + "You win!")
    else:
        print("Paper covers rock!"+ "\033[36m" + "You lose.")
