# Ask the user for the following:
# 1. Ask the user for the price of a child and an adult meal and store these values properly into variables as floating point numbers.
# 2. Ask the user for the number of adults and children and store these values properly into variables as integers.
# 3. Compute and display the subtotal (you do not need to worry about the sales tax or rounding to two decimals at this point).

# Final requirements / Submission
# 1. Ask the user for the sales tax rate and store the value properly as a floating point number.
# 2. Compute and display the sales tax.
# 3. Compute and display the total.
# 4. Ask the user for the payment amount and store the value properly as a floating point number.
# 5. Compute and display the change.
# 6. Include the appropriate currency symbol (for example $, €, etc.) before each displayed value.
# 7. Display each value to two decimals.
# 8. Double check that the calculations are correct.
# 9. Show creativity and exceed the core requirements by adding additional features.
# 10. Use good style in your program, including variable names and whitespace.

# Qstn : how to run the code without having to run the whole program?

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
# print(s_rate)
taxSales = ( sub_cost * s_rate)
# print(taxSales)
total_cost = "Total: " + "$" + str(sub_cost + taxSales)
totalCost = sub_cost + taxSales
print(total_cost)
print()

amount_paid = float(input("What is the payment amount? "))
change = "Change: " + "$" + str(amount_paid - totalCost)
print(change + " \nEnjoy you meal!")
