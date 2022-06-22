import random
from os import system


def logo():
    return '''
 _______           _______  _______  _______   _________          _______    _                 _______  ______   _______  _______   
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  \__   __/|\     /|(  ____ \  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )  
| (    \/| )   ( || (    \/| (    \/| (    \/     ) (   | )   ( || (    \/  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|  
| |      | |   | || (__    | (_____ | (_____      | |   | (___) || (__      |   \ | || |   | || || || || (__/ / | (__    | (____)|  
| | ____ | |   | ||  __)   (_____  )(_____  )     | |   |  ___  ||  __)     | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)  
| | \_  )| |   | || (            ) |      ) |     | |   | (   ) || (        | | \   || |   | || |   | || (  \ \ | (      | (\ (     
| (___) || (___) || (____/\/\____) |/\____) |     | |   | )   ( || (____/\  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__  
(_______)(_______)(_______/\_______)\_______)     )_(   |/     \|(_______/  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/  
                                                                                                                                    
\n'''


def game():
    print("Welcome to the Number Guessing Game!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return difficulty


def number_generator():
    number = random.randrange(1, 100)
    return number


def easy(difficulty, number):
    attempts = 10
    while (attempts > 0):
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        elif guess == number:
            return "Correct!"
        attempts -= 1
    return f"You lost. The number was {number}"


def hard(difficulty, number):
    attempts = 5
    while (attempts > 0):
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        elif guess == number:
            return "Correct!"
        attempts -= 1
    return f"You lost. The number was {number}"


play = 'yes'
while (play == "yes"):
    system('clear')
    print(logo())
    difficulty = game()
    number = number_generator()
    if difficulty == "easy":
        print(easy(difficulty, number))
    elif difficulty == "hard":
        print(hard(difficulty, number))
    play = input("Do you want to play again? Type 'yes' or 'no': ")
