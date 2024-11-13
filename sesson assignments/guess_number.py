import random

def main():
    # Generate the secret number at random
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Start the guessing loop
    guess = int(input("Enter a guess: "))  # Get the user's initial guess
    
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Ask for a new guess if the previous one was incorrect
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
    
    # Congratulate the user once they guess correctly
    print(f"Congrats! The number was: {secret_number}")

if __name__ == '__main__':
    main()