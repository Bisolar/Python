# Create a dictionary for a product with the following keys
# name
# price
# qunatity
# color
# # image _link

# product = {"name" : "Polo_Jacket",
#            "price" : 34.56,
#            "quantity" : 1000,
#            "color" : "Red",
#            "image_link": "http//:rtfghy.mae.com",
#            "available" : True
# }
# # product["rating"] = 5.00
# # print(product)

# # del product["image_link"]
# # print(product)

# product.pop("image_link")
# print(product)

# product = {"id": 10,
#            "title": "HP Pavilion 15-DK1056WM",
#            "description": "HP Pavilion 15-DK1056WM Gaming...",
#            "price": 1099,
#            "discountPercentage": 6.18,
#            "rating": 4.43,
#            "stock": 89,
#            "brand": "HP Pavilion",
#            "category": "laptops",
#            "thumbnail": "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg",
#            "images": ["https://cdn.dummyjson.com/product-images/10/1.jpg", 
#                       "https://cdn.dummyjson.com/product-images/10/2.jpg",
#                       "https://cdn.dummyjson.com/product-images/10/3.jpg"]
# }

# img = product["images"]
# for image in img:
#     print(image)

# Exercise 1. Dictionary Creation
# Create a dictionary that maps country names to their capitals. 
# Write a program that prints each country and its capital.

# countries = {"Nigeria" : "Abuja",
#              "Ghana" : "Accra",
#              "Canada" : "Ottawa",
#              "Germany" : "Berlin",
#              }

# # Loop through the dictionary and print each country with its capital
# print("Countries and their capitals:")
# for country, capital in countries.items():
#     print(f"{country}: {capital}")

# Exercise 2. Dictionary Update
# Given a dictionary of students and their grades, write a program that updates a student's grade. 
# Allow the user to enter the student's name and the new grade.

# student_grade = {"Dami" : "Grade A",
#                  "Abisola" : "Grade B",
#                  "Asher" : "Grade A",
# }

# # Collect input from the user to update a student's grade
# student_name = input("Enter the student's name to update the grade: ")

# # Check if the student is in the dictionary
# if student_name in student_grade:
#     new_grade = input(f"Enter the new grade for {student_name}: ")
#     # Update the grade in the dictionary
#     student_grade[student_name] = new_grade
#     print(f"The grade for {student_name} has been updated to {new_grade}.")
# else:
#     print(f"{student_name} not found in the list of students.")

# # Print the updated dictionary
# print("Updated student grades:", student_grade)

# Exercise 3. Dictionary Looping
# Write a program that loops through a dictionary of products and their prices, and then prints each product with its price.
# products = {"Pepsi" : 350,
#             "Fanta" : 400,
#             "SevenUp" : 350
# }

# for pro, prices in products.items():
#     print(f"{pro} : {prices}")

# Exercise 4. Dictionary Key Search
# Write a program that checks if a given key exists in a dictionary. 
# Allow the user to enter the key to search for.
# dict = {"word1" : "Apple",
#         "word2" : "banana",
#         "word3" : "kiwi"
# }
# word_search = str(input("Please enter the word you are looking for \n>>"))
# if word_search in dict:
#     print(f"{word_search} is present")
# else:
#     print("Not Found")

# Exercise 5. Frequency Counter
# Write a program that counts the frequency of each letter in a given string. 
# Store the results in a dictionary where keys are letters, and values are the frequencies.
# Input string from the user
# input_string = input("Please enter a string: ")

# # Initialize an empty dictionary to store the frequency of each letter
# frequency_counter = {}

# # Iterate through each character in the string
# for char in input_string.lower():
#     if char.isalpha():  # Only count alphabetic characters
#         if char in frequency_counter:
#             frequency_counter[char] += 1  # Increment the count if the letter exists
#         else:
#             frequency_counter[char] = 1  # Initialize the count if the letter is new

# # Print the dictionary with the frequency of each letter
# print("Letter frequency in the given string:", frequency_counter)

# Exercise 6. Merge Dictionaries
# Write a program that merges two dictionaries into one. 
# Ensure that if a key exists in both dictionaries, the value from the second dictionary overrides the first.

# Exercise 7. Create a Nested Dictionary
# Create a dictionary that contains information about students and their courses. 
# Each student should have a list of courses they are enrolled in. 
# Write a program to add a new course to a student's list of courses.
# nested_dict = {"Asher" : {"course1" : "GNT101", "course2" : "MST011", "course3" : "CSR201"},
#                "Dami" : {"course1" : "GNT101", "course2" : "MST011", "course3" : "CSR201"},
#                "Abisola" :{"course1" : "GNT101", "course2" : "MST011", "course3" : "CSR201"}
# }

# nested_dict.update()

my_set = {1,2,3,4,5}

print(3 in my_set)