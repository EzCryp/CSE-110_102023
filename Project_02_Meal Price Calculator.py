# ask for an input value of the child and adult meal and drinks
childs_meal_cost = float(input("What is the price of a child's meal? "))
childs_drink = float(input("How much for the child's drinks? "))
print()
adults_meal_cost = float(input("What is the price of an adult's meal? "))
adults_drink = float(input("How much for the child's drinks? "))
print()

# ask for an input value of how many kids and adults
num_of_kids = int(input("How many children are there with meal and drinks? "))
num_of_adults = int(input("How many adults are there with meal and drinks? "))
meal_combine = (((childs_meal_cost + childs_drink) * num_of_kids) + ((adults_meal_cost + adults_drink) * num_of_adults))
print()
print(f"Subtotal: ${meal_combine: .2f}")
print()

# input the tax rate to compute the sale tax and then get the total cost by adding the subtotal and the sales tax
sales_rate = float(input("What is the sales tax rate? "))
sales_tax = meal_combine * (sales_rate/100)
total = meal_combine + sales_tax
print(f"Sales Tax:  ${sales_tax: .2f}")
print(f"Total: ${total: .2f}")
print()

# ask for an input value of how much money they are paying to compute for the change
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change: .2f}") 
# dont forget to closing greeetings
print("\nHave a wonderful day \nEnjoy your meal!")
