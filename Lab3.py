1. Python program to check leap year
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

2. Python program to find the largest among three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if (number1 > number2) and (number1 > number3):
    print(f"{number1} is the largest number.")
elif (number2 > number1) and (number2 > number3):
    print(f"{number2} is the largest number.")
else:
    print(f"{number3} is the largest number.")


3. Python program to check if a number is positive, negative, or zero
number = int(input("Enter the number: "))

if number == 0:
    print("The number is zero.")
elif number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

4. Toy Vendor Program
product_code = int(input("Enter the product code (1 for Battery, 2 for Key-based, 3 for Electrical): "))
order_amount = float(input("Enter the order amount: "))

if product_code == 1 and order_amount > 1000:
    discount = 0.10 * order_amount
elif product_code == 2 and order_amount > 100:
    discount = 0.05 * order_amount
elif product_code == 3 and order_amount > 500:
    discount = 0.10 * order_amount
else:
    discount = 0
net_amount = order_amount - discount
print(f"The net amount after discount is Rs. {net_amount}.")

5. Transport fare calculation
distance = float(input("Enter the distance traveled (in km): "))

if 1 <= distance <= 50:
    fare = distance * 8
elif 51 <= distance <= 100:
    fare = distance * 10
elif distance > 100:
    fare = distance * 12
else:
    fare = 0

if fare > 0:
    print(f"The total fare is Rs. {fare}.")
else:
    print("Invalid distance entered.")
