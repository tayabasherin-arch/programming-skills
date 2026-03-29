# Define the password and max attempts
password = "12345"
attempts_left = 5

# While loop continues until access is granted or attempts run out
while attempts_left > 0:

    # Ask the user for the password and show remaining attempts
    entry = input(f"Password required ({attempts_left} left): ")
    
    if entry == password:

        # If the password is correct, grant access and stop the loop
        print("Access Granted.")
        break
    else:
        # If wrong, take away one attempt
        attempts_left -= 1
        print("Wrong password.")

# Check if the user ran out of all attempts
if attempts_left == 0:

    # Show the message for maximum attempts reached
    print("Maximum attempts reached. Alerting the authorities!")