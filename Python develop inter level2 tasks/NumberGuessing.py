import random

def number_guesser(lower_bound, upper_bound):
    
    secret_number = random.randint(lower_bound, upper_bound)
    
    guess = None
    
    while guess != secret_number:
        
        guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    print(f"Congratulations! You've guessed the number {secret_number} correctly!")


lower_bound = 1
upper_bound = 100  
number_guesser(lower_bound, upper_bound)
