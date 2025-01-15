1] calculate the multiplication and addition of two numbers
# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Calculate multiplication and sum
multiplication = num1 * num2
summation = num1 + num2
print(f"The multiplication of {num1} and {num2} is {multiplication}.")
print(f"The sum of {num1} and {num2} is {summation}.")


2]Declare two variables and print that which variable is largest using ternary operators
# Declare two variables
a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))
# Determine the largest variable using a ternary operator
largest = a if a > b else b
print(f"The largest variable is {largest}.")


3]Convert the temperature in degree centigrade to Fahrenheit
# Input temperature in degree centigrade
celsius = float(input("Enter the temperature in Celsius: "))
# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F.")


4]Python program to find the area of a triangle whose sides are given.
import math
# Input the sides of the triangle
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))
# Calculate the semi-perimeter
s = (a + b + c) / 2
# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is {area:.2f} square units.")
