first_name = str(input("Enter your First Name:\n >> ")).upper()
last_name = str(input("Enter your Last Name:\n >> ")).upper()
username = str(input("Create your username:\n >> "))
age = int(input("How old are you?\n >> "))
Phone_number = int(input("Enter your phone number\n >> "))
password1 = input("Create a new password:\n >> ")
password2 = input("Confrim password: \n >> ")

if password1 == password2:
    print(f"Dear {first_name} {last_name} your account has been created\n Welcome to the family ")
else:
    print("Password does not match. Please try Again. ")