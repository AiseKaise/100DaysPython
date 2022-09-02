# Print 2 Celebrities Randomly 
from game_data import data
from art import logo
from art import vs
import random
import os

def format_data(account):
    """Format the account data in readable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and followers count and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
account_b = random.choice(data)

game_should_continue = True

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower() 

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system('cls')
    print(logo)

    if is_correct:
        score += 1
        print(f"Your right! Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Dorry, its wrong. Final Score: {score}")
            






