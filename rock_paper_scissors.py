# We will write a rock paper scissors game in class - Complete it in this file
import random 

player_choice="rock"
computer_choice="paper"

#create a function that gets the choices
def  get_choices():
    options= ["rock","paper","scissors"]
    player_choice= input("Enter a choice (rock,paper,scissors):")
    computer_choice= random.choice(options)
    
    choices={"player": player_choice, "computer": computer_choice}
    return choices

#function to check for a win
def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}") 
    if player==computer:
        return "It's a tie"
    elif player== "rock":
        if computer== "scissors":
            return "Rock smashes scissors, You win!"
        else:
            return "Paper covers rock, you lose :(("
result= check_win("rock","rock")
choices= get_choices()
#print(choices)