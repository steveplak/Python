import random

def main():
    print("Welcome to the Game, You will be paying Rock-Paper-Scissors against me! \n Good Luck!")
    Game()


def Game():
    guess = input("Rock, paper, or scisors? ").strip().lower()
    options = ["rock", "paper", "scisor"]
    Computer_guess = random.choice(options)
    print(f"computer chose {Computer_guess}")
    if guess == Computer_guess 


main()