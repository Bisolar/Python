pepsi = 350
mirinda = 350
seven_up =350

response = str(input("what would you like to buy? \n1. Pepsi \n2. Miranda\n3. 7up\n >>")).lower()

if response == "1" or response == "pepsi":
    print(f"Pepsi is {pepsi} \nHow many would you like to buy?")
    reply = int(input())
    