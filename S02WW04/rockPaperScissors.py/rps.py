from flask import Flask, render_template
#import random
from random import choice, randint

options = ["rock","paper","scissors"]
Enemy = choice(options)
print("Website is ", website)
    print("Player is ", player)
    if player == Enemy:
        print("Draw")
        return render_template("rps.html",player=player,website=website,result = "DRAW!!")
    elif player == "rock" and website == "scissors":
        print("Win")
        return render_template("rps.html",player=player,website=website,result = "YOU WINNN!")
    elif player == "paper" and website == "rock":
        print("Win")
        return render_template("rps.html",player=player,website=website,result = "YOU WINNN!")
    elif player == "scissors" and website == "paper":
        print("Winnner")
        return render_template("rps.html",player=player,website=website,result = "YOU WINNN!")
    else: 
        print("Looser")
        return render_template("rps.html",player=player,website=website,result = "....you lost...COMPUTER WINS!")