sms = str(input("Dial *737# to load options\n>> "))
while True:
    print("Welcome to GTBank!!!\n1. Airtime self\n2. Airtime others\n3. Data\n4. Transfer-GTB\n5. Transfer- Others\n6. Pay Bills\n7. Exit")
    user_choice = int(input("Please choose an option from (1-7)\n>> "))
        
    if user_choice == 1:
        amount = float(input("Please enter amount\n>> "))
        print(f"Account recharge of N{amount} was successful!")
        break
    elif user_choice == 2:
        thirdparty_number = int(input("Please enter third party Phone number\n>> "))
        thirdparty_amount = float(input("Please enter amount\n>> "))
        pin_code = int(input("Enter PIN\n>> "))  
        print(f"Account recharge for {thirdparty_number} with an amount of {thirdparty_amount} was successful.")
        break
    elif user_choice == 3:
        reply = int(input("Are you buying for:\n1. Self\n2. Third Party\n>> "))
        if reply == 1:
            reply2 = int(input("Please select bundle\n1. 500MB\n2. 1GB\n3. 2GB\n4. 5GB\n5. 10GB\n6. 20GB\n>>  "))
            print()
    elif user_choice == 4:
        account_number = int(input("Please enter Account number\n>> "))
        transfer_amount = float(input("Please enter amount\n>> "))
        pin_code = int(input("Enter PIN\n>> "))          #limit to four digits
        print(f"Your have successfully transferred NGN {transfer_amount} to {account_number}")
        break
    elif user_choice == 5:
        bank = str(input("Please select bank\n1. Access Bank\n2. First bank\n3. FCMB\n4. Zenith\n5. Others\n>> "))
        account_number = int(input("Please enter Account number\n>> "))
        transfer_amount = int(input("Please enter amount\n>> "))
        pin_code = int(input("Enter PIN\n>> "))          #limit to four digits
        print(f"Your have successfully transferred NGN {transfer_amount} to {account_number}")
        break
    elif user_choice == 6:
        bills = int(input("Please Select\n1. DSTV/GOTV\n2. Buy Prepaid Unit\n3. LAWMA\n4. Others\n>> "))
        break
    elif user_choice == 7:
        print("Thank you for using GTBank. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
        break