# Creating a meal calculator and adding beverages cost, appetizers, and tip percentage

childs_meal_cost = float(input("What is the price of a child's meal? "))
adults_meal_cost = float(input("What is the price of an adult's meal? "))

num_of_kids = int(input("How many children are there? "))
num_of_adults = int(input("How many adults are there? "))
print()
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
