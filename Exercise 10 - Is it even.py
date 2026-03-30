# Function to determine even or odd 
def check(number):
    
    # Checks if a number is even or odd using the modulo operator.
    if number % 2 == 0:

        # If the number divided by 2 has a remainder of 0, it is even
        return "The number is even." 
    
    # Otherwise, it must be odd
    else:
        return "The number is odd." 

# Main part of the program
def main():
    # Get the number from the user and convert it to an integer
    user_num = int(input("Enter a number: "))

    # Pass number to function and print returned message 
    result = check(user_num)
    print(result)

# Call main to start the program
if __name__ == "__main__":
    main()