# the value of the product
pepsi = 350
mirinda = 350
seven_up =350

response = str(input("what would you like to buy? \n1. Pepsi \n2. Miranda\n3. 7up\n >>")).lower()

#condition handling
if response == "1" or response == "pepsi":
    print(f"Pepsi is NGN {pepsi} \nHow many would you like to buy?")
    reply = int(input())
    total_cost = pepsi * reply
    print(f"Your total is NGN {total_cost}\nAre you paying with;\n1. Cash\n2. Card")
    reply2 = input()                     #user to input either cash or card
    if reply2 == "1" or reply2 == "cash":
        print("How much are you paying?")
        reply3 = int(input())          
        balance = reply3 - total_cost
        if balance == 0:
            print("Thank you for Shopping with us!!")
        elif balance > 0:
            print(f"Your Balance is NGN {balance}\nThank you for shopping with us")
        else:
            print("Please enter a valid payment")
    elif reply2 == "2" or reply2 == "card":
        print("Please enter your card details:")
        card_number = input("Card number: ")      #limit card number to 16 digits
        expiry_date = input("Expiry date (MM/YY): ")
        cvv = input("CVV: ")                       #limit CVV to three digits
        print("Your Payment is Successful!\nThank you for Shopping with us!")
    else:
        print("You have entered an invalid input, Try Again!")
elif response == "2" or response == "mirinda":
    print(f"Mirinda is NGN {mirinda} \nHow many would you like to buy?")
    reply = int(input())
    total_cost = mirinda * reply
    print(f"Your total is NGN {total_cost}\nAre you paying with;\n1. Cash\n2. Card")
    reply2 = input()                     #user to input either cash or card
    if reply2 == "1" or reply2 == "cash":
        print("How much are you paying?")
        reply3 = int(input())          
        balance = reply3 - total_cost
        if balance == 0:
            print("Thank you for Shopping with us!!")
        elif balance > 0:
            print(f"Your Balance is NGN {balance}\nThank you for shopping with us")
        else:
            print("Please enter a valid payment")
    elif reply2 == "2" or reply2 == "card":
        print("Please enter your card details:")
        card_number = input("Card number: ")      #limit card number to 16 digits
        expiry_date = input("Expiry date (MM/YY): ")
        cvv = input("CVV: ")                       #limit CVV to three digits
        print("Your Payment is Successful!\nThank you for Shopping with us!")
    else:
        print("You have entered an invalid input, Try Again!")
elif response == "3" or response == "7up":
    print(f"7up is NGN {seven_up} \nHow many would you like to buy?")
    reply = int(input())
    total_cost = seven_up * reply
    print(f"Your total is NGN {total_cost}\nAre you paying with;\n1. Cash\n2. Card")
    reply2 = input()                     #user to input either cash or card
    if reply2 == "1" or reply2 == "cash":
        print("How much are you paying?")
        reply3 = int(input())          
        balance = reply3 - total_cost
        if balance == 0:
            print("Thank you for Shopping with us!!")
        elif balance > 0:
            print(f"Your Balance is NGN {balance}\nThank you for shopping with us")
        else:
            print("Please enter a valid payment")
    elif reply2 == "2" or reply2 == "card":
        print("Please enter your card details:")
        card_number = input("Card number: ")      #limit card number to 16 digits
        expiry_date = input("Expiry date (MM/YY): ")
        cvv = input("CVV: ")                       #limit CVV to three digits
        print("Your Payment is Successful!\nThank you for Shopping with us!")
    else:
        print("You have entered an invalid input, Try Again!")
else:
    print("Invalid Request. Try Again!")