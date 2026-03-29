# Set up a dictionary with countries and their capitals
quiz = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid", "UK": "London"}

# Loop through the quiz items to ask questions
for country, capital in quiz.items():

    # Ask the user for the capital
    answer = input(f"What is the capital of {country}? ")
    
    # Check if the answer is correct regardless of capital letters
    if answer.lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Wrong! The answer is {capital}")