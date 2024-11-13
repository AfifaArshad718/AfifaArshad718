def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))  # Get the number and convert it to an integer
    
    # Loop to double the value until it's 100 or greater
    while curr_value < 100:
        print(curr_value, end=" ")  # Print the current value followed by a space (not a newline)
        curr_value = curr_value * 2  # Double the current value
    
    # Print the final value when it exceeds 100 or is 100
    print(curr_value)  # This print is for the last value that exceeds or equals 100

# This ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()
