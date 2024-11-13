def access_element(my_list, index):
    """Access an element at a given index."""
    if index < 0 or index >= len(my_list):
        return "Index out of range."
    return my_list[index]

def modify_element(my_list, index, new_value):
    """Modify an element at a given index."""
    if index < 0 or index >= len(my_list):
        return "Index out of range."
    my_list[index] = new_value
    return my_list

def slice_list(my_list, start, end):
    """Return a slice of the list from start to end (exclusive)."""
    if start < 0 or end > len(my_list):
        return "Invalid range."
    return my_list[start:end]

def main():
    # Initialize a sample list for the game
    sample_list = ['apple', 'banana', 12, 45, 'grape']
    
    print("Welcome to the Index Game!")
    print("Here is your list:", sample_list)
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit game")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':  # Access an element
            index = int(input("Enter the index to access: "))
            result = access_element(sample_list, index)
            print("Result:", result)
        
        elif choice == '2':  # Modify an element
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(sample_list, index, new_value)
            print("Updated list:", result)
        
        elif choice == '3':  # Slice the list
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(sample_list, start, end)
            print("Sliced list:", result)
        
        elif choice == '4':  # Exit the game
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice. Please choose a valid operation.")
        
if __name__ == "__main__":
    main()
