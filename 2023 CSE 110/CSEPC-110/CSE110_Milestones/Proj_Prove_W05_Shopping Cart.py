""""
Author: Ezra Zacarias
Milestone: W05_Prove_Shopping Cart
"""
# In this assignment we will be making a list of codes for a shopping cart items.
# There will be MENU on what the user would want as an action item

# First let us print a welcome greeting for the user
print("Welcome to the Shopping Cart Program!\n")

# itemized option / menu for the shopping cart prove
menu = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

# provide a option number as an action button that will go along the menu
numbers = [1, 2, 3, 4, 5]

# create empty storage for items that will be put in the cart along with its price
cart_items = []
prices = []
total = 0

# the initial action number will be nothing
action_num = ""

# print the menu items with the number
# ask user to select a number serving as our action button
for i in range(len(menu)):
    print(numbers[i], menu[i])
action_num = int(input("\nPlease select one of the following: "))

# create a continous condition or while loop until condition are met
while True:
    while action_num == "":
        action_num = int(input("\nPlease select one of the following: "))

    #if the user select number 1, ask user to input add item
    while action_num == 1:
        add_item = input("What item would you like to add: \n")
        cart_items.append(add_item)
        print(f"\n'{add_item.upper()}' has been added to the cart.")

        # after the user input string of item, ask for the amout and include in the "prices" storage
        price = float(input(f"Enter the price of '{add_item.upper()}': $\n"))
        prices.append(price)
        print()

        # after condition number 1, print the Menu option again
        for i in range(len(menu)):
            print(numbers[i], menu[i])
        action_num = int(input(("\nPlease select one of the following:\n")))

    # if the user select the number 2, show or print what is in the cart
    while action_num == 2:
        print("----- IN YOUR CART -----\n")

        for item in cart_items:
            print(item, end="\n")
        print()
        
        # after condition number 2, print the Menu option again
        for i in range(len(menu)):
            print(numbers[i], menu[i])
        action_num = int(input(("\nPlease select one of the following:\n")))

    # if the user select the number 3, ask the user what item to remove
    while action_num == 3:
        rem_item = input(f"What item would you like to remove? ")
        cart_items.remove(rem_item)
        print(f"'{rem_item.upper()}' has just been removed to the cart.")
        prices.remove(rem_item)
        print()

        # after condition number 3, print the Menu option again
        for i in range(len(menu)):
            print(numbers[i], menu[i])
        action_num = int(input(("\nPlease select one of the following:\n")))

    # if the user select the number 4, print out the accumulated price
    while action_num == 4:
        for price in prices:
            total += price
        print(f"Your total is: ${total:.2f}\n")

        # after condition number 4, print the Menu option again
        for i in range(len(menu)):
            print(numbers[i], menu[i])
        action_num = int(input(("\nPlease select one of the following:\n")))

    # if the user select the number 5, print a closing greeting
    if action_num == 5:
        print("\nThank you for shopping with us! \nEnjoy your day!")
    break

# otherwise if all condition are not met, print a closing greeting
else:
    print("\nYou have not selected anything.\nThank you for shopping with us! \nEnjoy your day!")
