# """Tip function"""
# def tip_c(a):
#     tip = 0.1 * a
#     total = tip + a
#     return total



# def joint(a, b):
#     cost = a / b
#     return cost

# def balance(x, sas):
#     change = x - sas
#     if change == 0:
#         print("You don't have change")
#     else:
#         print(change)
        
# def main():
#     purchase = int(input("Good day :blush:, hope you enjoyed our service\nHow much was your total purchase\n\nWe charge 10% of your total purchase>>"))
#     total = tip_c(purchase)
#     response = str(input("What type of payment are you making\n(a.) Joint payment\n(.b) Single payment\n>>")).lower()
#     if response == 'a':
#         reply = int(input("How many of you are paying together\n>>"))
#         dam = joint(total, reply)
#         print(dam)
#     elif response == 'b':
#         print(total)
#     method = str(input("What type of payment are you making\n(a.) Cash\n(.b)Bank payment\n>>")).lower()
#     if method == 'a':
#         cash_hand = int("How much cash are you paying\n>>")
#         balance(cash_hand, total) 
#     elif method == 'b':
#         print("Done and debited")


# # Optimise the cost and handle the joint error


# def loan(p, r, t):
#    s_i =  (p * r * t)/100
#    return s_i

# loan(1100, 0.5, 60)

# cost = lambda x : x + 10
# print(cost(4))


x = lambda a: a **5

print(x(5))