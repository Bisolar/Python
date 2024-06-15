# def add_numbers(a, b):
#     c = a + b
#     return c

# a = 5
# b = 6
# c = add_numbers(a, b)
# print("The sum is ", c)

# def multipy_numbers(a, b):
#     c = a * b
#     return c

# a = 10
# b = 11
# c = multipy_numbers(a, b)
# print ("The product is", c)
    

# Exercise 1: Addition Function
# Write a function called add_numbers that takes two parameters a and b and returns their sum.
# define a function for adding numbers

# def add_num(a, b):
#     c = a + b
#     print(c)

# add_num(4, 5)

# Exercise 2: Multiplication Function
# Write a function called multiply_numbers that takes two parameters a and b and returns their product.
# def multiply_numbers(a, b):
#     c = a * b
#     print(c)
# multiply_numbers(3, 6)

# Exercise 3: Square Function
# Write a function called square_number that takes a parameter x and returns its square.
# def square_number(x):
#     y = x **2
#     print(y)
# square_number(7)

# Exercise 4: Power Function
# Write a function called power that takes two parameters base and exponent and returns the result of raising base to the power of exponent.
# def power(base, exponent):
#     result = base ** exponent
#     return result

# # Test the function
# print(power(2, 3))  # Output: 8
# print(power(5, 2))  # Output: 25

# Exercise 5: Maximum Function
# Write a function called find_maximum that takes a list of numbers as input and returns the maximum value in the list.
# def find_maximum(numbers):
#     if len(numbers) == 0:
#         return None  # Return None if the list is empty
#     max_num = numbers[0]  # Assume the first number is the maximum
#     for num in numbers:
#         if num > max_num:
#             max_num = num  # Update max_num if a larger number is found
#     return max_num

# # Test the function
# print(find_maximum([3, 7, 2, 9, 5]))  # Output: 9
# print(find_maximum([-1, -5, -3]))     # Output: -1
# print(find_maximum([]))               # Output: None

# Exercise 6: Factorial Function
# Write a function called factorial that takes an integer n as input and returns the factorial of n.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result

# # Test the function
# print(factorial(5))  # Output: 120
# print(factorial(0))  # Output: 1
# print(factorial(1))  # Output: 1


# Exercise 7: Check Even or Odd Function
# Write a function called is_even that takes an integer n as input and returns True if n is even and False otherwise.
# def is_even(n):
#     if n % 2 ==0:
#         return True
#     else:
#         return False

# print(is_even(5))
# print(is_even(6))
# print(is_even(11))

# Exercise 8: Greeting Function
# Write a function called greet that takes a parameter name and returns a personalized greeting message.
# def greet(name):
#     print("Hello", name)

# greet(name = "Amy")
# or
# def greet(name):
#     return f"Hello, {name}!"

# # Test the function
# print(greet("Amy"))  # Output: Hello, Amy!

# Exercise 9: Temperature Conversion Function
# Write a function called convert_to_celsius that takes a temperature in
# Fahrenheit as input and returns the equivalent temperature in Celsius.
# def convert_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5 / 9
#     return celsius

# # Test the function
# fahrenheit_temp = 98.6
# print(f"{fahrenheit_temp} Fahrenheit is equal to {convert_to_celsius(fahrenheit_temp)} Celsius")

# Exercise 10: Area of Circle Function
# Write a function called calculate_area_of_circle that takes the radius of a circle as input and returns its area.
# import math

# def calculate_area_of_circle(radius):
#     area = math.pi * (radius ** 2)
#     return area

# # Test the function
# radius = 5
# print(f"The area of a circle with radius {radius} is {calculate_area_of_circle(radius)}")



            

