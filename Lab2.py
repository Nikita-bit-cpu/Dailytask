1. Check whether the number is even or odd using a ternary operator
# Input a number from the user
num = int(input("Enter a number: "))
# Check if the number is even or odd using a ternary operator
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}.")


2. Swap two numbers taken from the user
# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
# Swap the numbers
num1, num2 = num2, num1
print(f"After swapping: num1 = {num1}, num2 = {num2}")


3. Convert kilometers to miles
# Input distance in kilometers
kilometers = float(input("Enter distance in kilometers: "))
# Convert kilometers to miles (1 km = 0.621371 miles)
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")


4. Find the Simple Interest with user input
# Input principal, time, and rate from the user
principal = float(input("Enter the principal amount (Rs.): "))
time = float(input("Enter the time (in years): "))
rate = float(input("Enter the rate of interest (in %): "))
# Calculate simple interest
simple_interest = (principal * time * rate) / 100
print(f"The simple interest on Rs. {principal} for {time} years at {rate}% per year is Rs. {simple_interest:.2f}.")

 
