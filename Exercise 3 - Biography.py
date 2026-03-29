# Creating a dictionary to store the personal information
personal_info = {
    "Name": "Tayaba Sherin",
    "Hometown": "Ajman",
    "Age": 18
}

# Printing these values on separate lines using a single print statement
print(f"Name: {personal_info['Name']}\nHometown: {personal_info['Hometown']}\nAge: {personal_info['Age']}")

#  The user is asked to enter their full name and store it in the variable 'Name'
Name = input("Enter your full name: ")

# The user is asked to enter their hometown and store it in the variable 'Hometown'
Hometown = input("Enter your hometown: ")

# The user is asked to enter their age and store it in the variable 'Age_input'
Age_input = input("Enter your age: ")

# Check if the age entered by the user is a number to prevent errors with string inputs
if Age_input.isdigit():

    # If it is, the Age_input variable is converted to an integer and stored in 'Age'
    Age = int(Age_input)

    # Create a second dictionary to store the user provided data
    personal_info2 = {
        "Name": Name,
        "Hometown": Hometown,
        "Age": Age
    }

    # The details are then printed on separate lines using a single print statement
    print(f"Name: {personal_info2['Name']}\nHometown: {personal_info2['Hometown']}\nAge: {personal_info2['Age']}")
else:

    # If it’s not a number, an error message is displayed
    print("Please enter a numeric value for age.")