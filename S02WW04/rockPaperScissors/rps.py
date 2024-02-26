from flask import Flask, render_template
#import random
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def main():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if player_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(player_choice, computer_choice))
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
