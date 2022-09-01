from random import * 
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(gen_random_num, guess, turns):
    """checks answers against guess. Returns the number of turns remaining"""
    if gen_random_num > guess:
        print("Too Low.")
        return turns - 1
    elif gen_random_num < guess:
        print("Too High.")
        return turns - 1
    else:
        print(f"You got it!, The answer was {gen_random_num}.")

def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 - 100.")
    gen_random_num = randint(1, 100)
    # print(f"Pssst, the correct answer is {gen_random_num}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != gen_random_num:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(gen_random_num, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != gen_random_num:
            print("Guess again....")


game()