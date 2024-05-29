# # Define a function that returns the maximum of two numbers
# def max_of_two(x, y):
#     # Check if x is greater than y
#     if x > y:
#         # If x is greater, return x
#         return x
#     # If y is greater or equal to x, return y
#     return y

# # Define a function that returns the maximum of three numbers
# def max_of_three(x, y, z):
#     # Call max_of_two function to find the maximum of y and z,
#     # then compare it with x to find the overall maximum
#     return max_of_two(x, max_of_two(y, z))

# # Print the result of calling max_of_three function with arguments 3, 6, and -5
# print(max_of_three(3, 6, -5)) 

# # Define a function named 'sum' that takes a list of numbers as input
# def sum(numbers):
#     # Initialize a variable 'total' to store the sum of numbers, starting at 0
#     total = 0
    
#     # Iterate through each element 'x' in the 'numbers' list
#     for x in numbers:
#         # Add the current element 'x' to the 'total'
#         total += x
    
#     # Return the final sum stored in the 'total' variable
#     return total

# # Print the result of calling the 'sum' function with a tuple of numbers (8, 2, 3, 0, 7)
# print(sum((8, 2, 3, 0, 7))) 


