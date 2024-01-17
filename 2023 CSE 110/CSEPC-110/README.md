# CSEPC-110-Meal-Calculator
Meal Calculator

# Creating a meal calculator and adding beverages cost, appetizers, and tip percentage

# Create a variable where you can store the value of the childs meal cost
childs_meal_cost = float(input("What is the price of a child's meal? "))

# Create a variable where you can store the value of the childs meal cost
adults_meal_cost = float(input("What is the price of an adult's meal? "))

# Asking for user how many kids
num_of_kids = int(input("How many children are there? "))

# Asking for user how many kids
num_of_adults = int(input("How many adults are there? "))
print()

# Computing the subtotal by multiplying the kids and adults meal cost to the number of kids and adults
subtotal = "Subtotal: " + "$" + str((childs_meal_cost * num_of_kids) + (adults_meal_cost * num_of_adults))
print(subtotal)
sub_cost = float((childs_meal_cost * num_of_kids) + (adults_meal_cost * num_of_adults))
print()

sales_rate = float(input("What is the sales tax rate? "))
s_rate = (sales_rate / 100)
taxSales = ( sub_cost * s_rate)
total_cost = "Total: " + "$" + str(sub_cost + taxSales)
totalCost = sub_cost + taxSales
print(total_cost)
print()

amount_paid = float(input("What is the payment amount? "))
change = "Change: " + "$" + str(amount_paid - totalCost)
print(change + " \nHave a wonderful day \nEnjoy you meal!")
