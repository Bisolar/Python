# first_name = str(input("Enter your First Name:\n >> ")).upper()
# last_name = str(input("Enter your Last Name:\n >> ")).upper()
# username = str(input("Create your username:\n >> "))
# age = int(input("How old are you?\n >> "))
# Phone_number = int(input("Enter your phone number\n >> "))
# password1 = input("Create a new password:\n >> ")
# password2 = input("Confrim password: \n >> ")

# if password1 == password2:
#     print(f"Dear {first_name} {last_name} your account has been created\n Welcome to the family ")
# else:
#     print("Password does not match. Please try Again. ")

# Product prices
PRODUCT_PRICES = {
    "pepsi": 350,
    "mirinda": 350,
    "7up": 350
}

def calculate_total_cost(product, quantity):
    return PRODUCT_PRICES[product] * quantity

def process_payment(total_cost):
    payment_method = input("Are you paying with:\n1. Cash\n2. Card\n >>")
    if payment_method.lower() == "cash":
        amount_paid = int(input("How much are you paying? "))
        balance = amount_paid - total_cost
        if balance >= 0:
            print("Thank you for shopping with us!")
            if balance > 0:
                print(f"Your change: NGN {balance}")
        else:
            print("Insufficient payment. Please enter a valid amount.")
    elif payment_method.lower() == "card":
        card_number = input("Card number: ")
        expiry_date = input("Expiry date (MM/YY): ")
        cvv = input("CVV: ")
        print("Your payment is successful. Thank you for shopping with us!")
    else:
        print("Invalid payment method. Please enter 'cash' or 'card'.")

def main():
    print("Welcome to the shop!")
    print("What would you like to buy?")
    print("1. Pepsi\n2. Mirinda\n3. 7UP")
    product = input(">> ").lower()
    if product in PRODUCT_PRICES:
        quantity = int(input(f"How many {product.capitalize()} would you like to buy? "))
        total_cost = calculate_total_cost(product, quantity)
        print(f"Your total is NGN {total_cost}")
        process_payment(total_cost)
    else:
        print("Invalid product selection. Please try again.")

if __name__ == "__main__":
    main()

