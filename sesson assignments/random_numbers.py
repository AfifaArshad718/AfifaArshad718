import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Loop to print N_NUMBERS random numbers
    for _ in range(N_NUMBERS):
        # Generate a random number between MIN_VALUE and MAX_VALUE (inclusive)
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

    # Print a newline after all numbers are printed
    print()

if __name__ == '__main__':
    main()
