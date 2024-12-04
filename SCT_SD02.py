import random

def guess_the_number():
    print("Welcome to the Number Guessing Game")
    print("I have chosen a number between 1 and 100.")
    print("can you guess what it is?")

    random_number=random.randint(1,100)
    guess=None
    attempts=0
    while guess!=random_number:
        try:
            guess=int(input("Enter your guess"))
            attempts+=1
            if guess<random_number:
                print("Too low! try again.")
            elif guess>random_number:
                print("Too high! try again.")
            else:
              print(f"Congratulations! You guessed it in {attempts} attempts!")
        except ValueError:
            print("Please enter a valid number")

guess_the_number()
