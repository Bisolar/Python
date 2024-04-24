# car game with navigation keys
print("Welcome to your car race!! ")

while True:
    gamer_input = str(input("Select Navigation keys to move\nL = Left \nR = Right\nF = Forward\nB = backward\n >>")).upper()
    if gamer_input == "L":
        print("←←←←←")
    elif gamer_input == "R":
        print("➜➜➜➜➜")
    elif gamer_input == "F":
        print("↑↑↑↑↑")
    elif gamer_input == "B":
        print("↓↓↓↓↓")
        break
    else:
        print("Invalid Input! Try Again")