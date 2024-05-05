# create a list of vowels using the list constructor and print them out individually

vowel = ["a", "e", "i", "o", "u"]

# for v in vowel:
#     print(v)

# print(list(vowel))

# Assignment create a program that check if a word is has vowel
# collect input from user to check if the word has a vowel

user_input = str(input("Enter a word\n>> "))

# Variable to track if a vowel is found
has_vowel = False
# Check if the word contains a vowel
for letter in user_input:
    if letter in vowel:
        has_vowel = True
        break  # Exit the loop as soon as a vowel is found

# Print the result
if has_vowel:
    print(f"The word '{user_input}' contains a vowel.")
else:
    print(f"The word '{user_input}' does not contain any vowels.")


# Exercise 1 List Creation and Modification
# Create a list of your favorite fruits.
# Add a new fruit to the list.
# Remove one fruit from the list.
# Replace the second item in the list with another fruit.

# fruits = ["apples", "berries", "kiwis", "nuts"]
# # fruits.append("banana")
# # fruits.remove("apples")
# fruits.insert(3, "grapes")
# print(fruits)

# Exercise 2 List Iteration
# Write a program to iterate through a list of numbers and print each one.
# Iterate through a list of names and print each name with a greeting.
# num = [1, 2, 5, 7, 9, 3, 4]
# for n in num:
#     print(n)
# names = ["Dami", "Asher", "Abisola"]
# for n in names:
#     print("Hello, " + n)

# Exercise 3 Find the Maximum
# Write a program that finds the maximum number in a list of numbers.
# Modify the program to find the minimum number.
# num = [1, 2, 3, 7, 9, 10, 34, 54, 23, 12, 64]
# # num.sort()
# print(num.index(64))
# # print(num)
# maximum = max(num)
# print("The maximum number is:", maximum)
# minimum = min(num)
# print("The maximum number is:", minimum)

# Exercise 4 Sum of List Elements
# Create a list of integers and calculate the sum of all elements.
# Create a list of prices and calculate the total cost.
# list_integers = [2, 3, 5, 23, 19, 34]
# sum = sum(list_integers)
# print("The sum is:",sum)
# lists_prices = [23.00, 45.85, 12.34, 90.00, 12.50, 40]
# sum = sum(lists_prices)
# print("Your Total cost is NGN",sum)

# Exercise 5 List Slicing
# Given a list of numbers from 1 to 10, create a new list with the first five numbers.
# Create another list with the last five numbers.
# numbers = list(range(1, 11))
# first_five = numbers[:5]
# last_five = numbers[5:]
# print("The first five numbers:", first_five)
# print("The lasst five numbers:", last_five)

# Exercise 6 List Concatenation
# Create two separate lists and concatenate them into a third list.
# Add more elements to the third list.
# a = [4, 5, 6, 7]
# b = [3, 8, 9]
# c = a + b
# new = ["a", "b", "c"]
# print(c + new)

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("apple")
# fruits.insert(0, "kiwis")
# fruits.append("orange")
# fruits.insert(1, "lemon")
# fruits.remove("banana")
# print(len(fruits))

# Exercise 7 Remove Duplicates
# Write a program that removes duplicate elements from a list.
# Test the program with a list containing repeated numbers or words.

# Exercise 1 again . List of Even Numbers
# Write a program that creates a list of even numbers from 1 to 50. 
# Use a for loop to generate the list and an if condition to filter the even numbers.
# even_numbers = []
# # Iterate over the range from 1 to 50
# for i in range(1, 51):
#     # Check if the current number is even
#     if i % 2 == 0:
#         # If it's even, add it to the list
#         even_numbers.append(i)
#         even_numbers.

# # Print the list of even numbers
# print("List of even numbers from 1 to 50:", even_numbers)
# numbers = list(range(1, 51))
# even_numbers = [ ]

# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)

# print(even_numbers)

# Exercise 2 Find Prime Numbers
# Write a program that creates a list of prime numbers from 1 to 100. 
# Use a for loop to iterate over the numbers and a nested loop to check if a number is prime.
# prime_numbers = [ ]

# for i in range(2, 101):
#     if (i % i) == 1:
#         prime_numbers.append(i)
# print(prime_numbers)

# Exercise 3. Remove Duplicates
# Write a program that removes duplicate elements from a list. 
# Use a while loop to iterate through the list and remove duplicate values using an if condition.

# 4. List Reversal
# Write a program that reverses a list of elements without using built-in functions. 
# Use a while loop to swap elements from both ends of the list.
# Define a list of elements to reverse
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Initialize two pointers
# left = 0  # Start of the list
# right = len(my_list) - 1  # End of the list

# # Use a while loop to swap elements from both ends
# while left < right:
#     # Swap elements
#     my_list[left], my_list[right] = my_list[right], my_list[left]

#     # Move the pointers toward the center
#     left += 1
#     right -= 1

# # Print the reversed list
# print("Reversed list:", my_list)
