#grade = int(input("Enter your grade:\n >> "))

# #if grade >= 90:
#    print("Your grade is A")
#elif grade >= 80:
#    print("Your Grade is B")
#elif grade >= 70:
#    print("Your Grade is C")
#elif grade >= 60:
#   print("Your Grade is D")
#elif grade < 60:
#    print("Your Grade is F")
#else:
#    print("Please Enter the right figure")



#name = str(input("Please enter your name\n >>"))
#age = int(input("Please enter your age:\n >>"))

#if age < 12:
#    print(f"{name}, Your ticket price is $5")
#elif age <= 64:
#    print(f"{name}, Your ticket price is $10")
#elif age > 65:
#    print(f"{name}, Your ticket price is $7")
#else:
#    print("Your input is invalid. Please try again")


##number = int(input("Enter a number:\n >> "))

#if number == 0:
#    print(Zero)
#elif number < 0:
#    print("Negative Number")
#else:
#    print("Positive Number")

#letter = input("Enter a single letter:\n>> ").lower()  # Convert input to lowercase for case-insensitive comparison

#if len(letter) != 1 or not letter.isalpha():
#    print("Invalid input. Please enter a single letter.")
#elif letter in 'aeiou':
#    print("Vowel")
#else:
#    print("Consonant")



#year = int(input("Enter year:\n>> "))

#if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#    print(f"{year} is a leap year")
#else:
#   print(f"{year} is not a leap year")


#side1 = float(input("Enter the length of side 1:\n>> "))
#side2 = float(input("Enter the length of side 2:\n>> "))
#side3 = float(input("Enter the length of side 3:\n>> "))

#if side1 == side2 == side3:
#    print("It's an equilateral triangle.")
#elif side1 == side2 or side1 == side3 or side2 == side3:
#    print("It's an isosceles triangle.")
#else:
#    print("It's a scalene triangle.")


#def celsius_to_fahrenheit(celsius):
#    return (celsius * 9/5) + 32
#
#def fahrenheit_to_celsius(fahrenheit):
#    return (fahrenheit - 32) * 5/9
#
#print("Temperature Converter")
#print("2. Fahrenheit to Celsius")
##
#choice = input("Enter your choice (1 or 2):\n>> ")
#
#if choice == '1':
#   celsius = float(input("Enter temperature in Celsius:\n>> "))
#   fahrenheit = celsius_to_fahrenheit(celsius)
#elif choice == '2':
#    fahrenheit = float(input("Enter temperature in Fahrenheit:\n>> "))
#    celsius = fahrenheit_to_celsius(fahrenheit)
#    print(f"{fahrenheit}°F is equal to {celsius}°C")
#else:
#   print("Invalid choice. Please enter either 1 or 2.")


#number = int(input("Enter a number:\n >> "))

#    print("Zero")
#elif number < 0:
#    if number % 2 == 0:
#        print("Negative Number and even")
#    else:
#        print("Negative Number and odd")
#else:
#    if number % 2 == 0:
#        print("Positive Number and even")
#    else:
#        print("Positive Number and odd")


#age = int(input("Please enter your age\n >>"))
#
#if age <= 2:
#    print("Infant")
#elif age <= 5:
#    print("Toddler")
#elif age <= 12:
#    print("Child")
#elif age <= 17:
#    print("Teenager")
#else:
#    print("Adult")

#def apply_discount(total_cost, age):
#    if age <= 5:
#        discount = 0.20  # 20% discount for age 5 or below
#    elif 6 <= age <= 12:
#        discount = 0.10  # 10% discount for ages 6-12
#    elif age >= 60:
#        discount = 0.15  # 15% discount for age 60 or above
#    else:
#        discount = 0      # No discount for other ages
#    
#    discounted_price = total_cost * (1 - discount)
#   return discounted_price
#
#def main():
#    total_cost = float(input("Enter the total cost of items purchased: $"))
#    age = int(input("Enter your age: "))
#    
#    discounted_price = apply_discount(total_cost, age)
#    print(f"Discounted Price: ${discounted_price:.2f}")
#
#if __name__ == "__main__":
#    main()



# # Prompt the user to enter two numbers and an operator
# num1 = float(input("Enter the first number: "))
# operator = input("Enter the operator (+, -, *, /): ")
# num2 = float(input("Enter the second number: "))

# # Perform the corresponding arithmetic operation based on the operator
# if operator == '+':
#     result = num1 + num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '/':
#     # Check if the second number is not zero to avoid division by zero error
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         print("Error: Division by zero")
#         exit()  # Exit the program if division by zero occurs
# else:
#     print("Error: Invalid operator")
#     exit()  # Exit the program if an invalid operator is entered

# # Print the result of the arithmetic operation
# print(f"Result: {num1} {operator} {num2} = {result}")


# def multiplication_table(number):
#     print(f"Multiplication Table for {number}:")
#     for i in range(1, 11):
#         print(f"{number} * {i} = {number * i}")

# if __name__ == "__main__":
#     try:
#         num = int(input("Enter a number: "))
#         multiplication_table(num)
#     except ValueError
#         print("Invalid input. Please enter a valid number.")


# num1 = int(input("Enter first number:\n >>"))
# num2 = int(input("Enter Second Number:\n >>"))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num1} is lesser than {num2}")
# elif num1 == num2:
#     print(f"{num1} is equal to {num2}")
# else:
#     print("Invalid Input. Try again")


# num = int(input("Enter number\n >>"))

# if num > 0:
#     print("Positive Number")
# elif num < 0:
#     print("Negative Number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Invalid Input. Try again")

# num = int(input("Enter a number\n >>"))

# if num % 2 == 0:
#     print("Even number")
# elif num % 2 != 0:
#     print("Odd Number")

# grade = input("Please enter your grade\n >>").upper()

# if grade == "A":
#     print("Excellent!")
# elif grade == "B":
#     print("Good job!")
# elif grade == "C":
#     print("Passing.")
# elif grade == "D":
#     print("Barely passing.")
# elif grade == "F":
#     print("Not good.")
# else:
#     print("Invalid Input")

year = int(input("Enter year\n >>"))

if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not a Leap year")
