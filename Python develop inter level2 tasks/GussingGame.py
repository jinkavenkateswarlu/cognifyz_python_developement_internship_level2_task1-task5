import random

def guessing_game():
    
    secret_number = random.randint(1, 100)
    
   
    guess = 0
    
    
    while guess != secret_number:
       
        guess = int(input("Guess the number between 1 and 100: "))
        
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    
    print(f"Congratulations! You've guessed the number {secret_number} correctly!")

guessing_game()
