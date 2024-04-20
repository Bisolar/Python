"""While loop"""
while True:
    secret_number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess == secret_number:
            print("You win!!!")
            break
        else:
            print("You lost!!!!")
            
    if guess == secret_number:
        response = input("Would you like to play again?\na. Yes\nb. No\n>> ").lower()
        if response == "a" or response == "yes":
            continue  
        elif response == "b" or response == "no":
            break
        else:
            break 
    else:
        response = input("Would you like to play again?\na. Yes\nb. No\n>> ").lower()
        if response == "a" or response == "yes":
            continue  
        elif response == "b" or response == "no":
            break
        else:
            break

"""Nested loop"""
integer = list(range(5, 10))

print("Virtual score result")
for i in integer:
    for x in integer:
        print(f'Team1 {i} - {x} Team2')

"""For loop & nested loop"""
a = range(10)
for x in a:
    print(x)