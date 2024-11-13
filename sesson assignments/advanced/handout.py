import random

# Constants
NUM_ROUNDS = 5  # Number of rounds in the game
MIN_VALUE = 1   # Minimum number for the random number generator
MAX_VALUE = 100 # Maximum number for the random number generator

def main():
    # Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Initialize score
    score = 0
    
    # Loop through the rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        
        # Generate random numbers for the user and the computer
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)
        user_number = random.randint(MIN_VALUE, MAX_VALUE)
        
        # Show the user's number (but not the computer's)
        print(f"Your number is {user_number}")
        
        # Get the user's guess (higher or lower)
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Validate input
        while guess not in ["higher", "lower"]:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Game logic to check if the guess was correct
        if guess == "higher" and user_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif guess == "lower" and user_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Display the current score
        print(f"Your score is now {score}")
    
    # End game message and final score
    print("\nThanks for playing!")
    print(f"Your final score is {score}")

    # Conditional ending messages based on the score
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()

