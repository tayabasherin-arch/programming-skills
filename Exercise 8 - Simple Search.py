# Initialize the list of names with specific casing
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Part 1: Automatic Search for Sam 
# Check if "Sam" exists in the list (case-insensitive)
if "sam" in [name.lower() for name in names]:
    print("Sam was found in the initial list check!")
else:
    print("Sam was not found in the initial list check.")

# Part 2: User Input Search 
# Ask the user what name to look for and store it in target
target = input("Now, enter a name you want to search for: ")

# Create a new list where all names are lowercase for easier searching
names_lower = [name.lower() for name in names]

# Check if the lowercase version of the input exists in the lowercase list
if target.lower() in names_lower:

    # If a match is found, print a success message using the user's input
    print(f"Found {target} in the list!")
else:
    # If no match is found, print a failure message
    print(f"{target} is not in the list.")