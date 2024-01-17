""""
Author: Ezra Zacarias
Milestone: W05_Shopping Cart
"""
# In this assignment we will be making a list of items that you can do on your shopping cart
# There will be MENU on what the user would want as an action item
# First let us show a welcome greeting for the shopping cart program
print("Welcome to the Shopping Cart Program!\n")

# itemized option / menu is the shopping cart list
menu = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

# provide a number
numbers = [1, 2, 3, 4, 5]

# shopping_cart_items.sort()
shopping_cart_items = []
prices = []
total = 0

# Ask the user to select from the main menu
print("Please select one of the following: (from 1 - 5)")
for i in range(len(menu)):
    print(numbers[i], menu[i])

# create an empty variable for the selection
action_num = ""
action_num = int(input(("Please enter an action: \n")))

while True:
    if action_num == 1:
        add_item = input("What item would you like to add: \n")
        shopping_cart_items.append(add_item)
        price = float(input(f"Enter the price of {add_item}: $\n"))
        prices.append(price)

        if add_item == "":
            print("You did not add anything")
            add_item2 = input("Is there anything else? ")
            price = float(input(f"Enter the price of {add_item2}: $\n"))
            shopping_cart_items.append(add_item2)
            prices.append(price)

        # else:
        #     respond = input(f"Would you like to go to MAIN MENU: (Y or N)\n")
        #     if respond.lower() == "Y":
        #         print("Please select one of the following: (from 1 - 5)")
        #         for i in range(len(menu)):
        #             print(numbers[i], menu[i])
        #     break
    # else:
    #     print(f"Would you like to go to the main Menu? (Y or N)")
    #     break

    elif action_num == 2:
        print("----- IN YOUR CART -----\n")
        print("There is nothing on your cart")
        # print(shopping_cart_items[])
        print()
        respond = input(f"Would you like to go to MAIN MENU: (Y or N)\n")
    else:
        respond = input(f"Would you like to go to MAIN MENU: (Y or N)")
        if  respond == "y":
            print("Please select one of the following: (from 1 - 5)")
            for i in range(len(menu)):
                print(numbers[i], menu[i])
        else:
            print("----- IN YOUR CART -----\n")
            print("There is nothing on your cart")

    if action_num == 3:
        rem_item = input(f"What item you would like to remove? ")
        shopping_cart_items.remove(rem_item)
        print("On your cart: ",shopping_cart_items)
        break
    else:
        print(f"Would you like to go to MAIN MENU: (Y or N)")
        break
    #
    # if action_num == 4:
    #     print(f"Total: ")
    #     break
    # else:
    #         print(f"Would you like to go to MAIN MENU: (Y or N)")
    #         break

else:
    print(f"GO TO MAIN MENU? (Y or N)")

