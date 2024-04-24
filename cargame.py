# car game with navigation keys

while True:
    print("Welcome to your car race!! ")
    gamer_input = str(input("Select Navigation keys to move\nL = Left \nR = Right\nF = Forward\nB = backward\n >>")).upper()
    if gamer_input == "L":
        print("←←←←←")
        break
    elif gamer_input == "R":
        print("➜➜➜➜➜")
        break
    elif gamer_input == "F":
        print("↑↑↑↑↑")
        break
    elif gamer_input == "B":
        print("↓↓↓↓↓")
        break
    else:
        print("Invalid Input! Try Again")