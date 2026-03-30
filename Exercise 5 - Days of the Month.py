# Create a dictionary 
month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Input handling 
month = int(input("Enter month number (1-12): "))

# Check and output with leap year adjustment 
if month == 2:
    leap = input("Is it a leap year? (yes/no): ").lower() 
    if leap == "yes":
        print("There are 29 days.") 
    else:
        print("There are 28 days.")
elif month in month_days:
    print(f"There are {month_days[month]} days.") 
else:
    print("Invalid month number.") 