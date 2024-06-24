# CODE SOFT TASK-04

# Rock , Paper , Scissors Game

import random
# Function to get the user's choice
def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Choose rock, paper, or scissors: ").lower()
    return choice

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "You win! Rock crushes scissors."
        else:
            return "You lose! Paper covers rock."
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win! Paper covers rock."
        else:
            return "You lose! Scissors cut paper."
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "You win! Scissors cut paper."
        else:
            return "You lose! Rock crushes scissors."

# Main game function
def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Have a nice day")
            break

# Start the game
if __name__ == "__main__":
    play_game()


