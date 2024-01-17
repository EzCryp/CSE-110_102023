# Ask users to enter a group of numbers to be added on the list
print("\nEnter a list of numbers, type 0 when finished.")

numbers_list = []
number = None
running_total = 0
ave = 0

# create a input loops for all the numbers to be inserted in the numbers list
while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers_list.append(number)

# Checking whether the input numbers are added to the numbers list
print(numbers_list)

# Print the sum of numbers in the numbers list
for value in numbers_list:
    running_total += value
print()        
print(f"The sum is: {running_total}")

# Getting the average by getting the sum and dividing it to the lenght of the numbers list
print(f"\ncount: {len(numbers_list)}\n")
print(f"\nThe average is: {running_total / len(numbers_list):.2f} \n ")

# Finding the largest number in the numbers list, first is by sorting
numbers_list.sort()
print(numbers_list)

largest_num = -1
for value in numbers_list:
    if value > largest_num:
        largest_num = value
print(f"\nThe largest number is: {largest_num}\n" )

# Finding the smallest number in the input numbers list
smallest_num = 999999
for value in numbers_list:
    if value > 0 and value < smallest_num:
        smallest_num = value
print(f"\nThe smallest number is: {smallest_num}\n")