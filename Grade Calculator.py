"""
Author: Ezra Zacarias
Purpose: Determine and display letter grades, including +/-
"""
# Ask for grade percentage to find is equivalent letter
grade = float(input('What is your grade percentage? '))
if grade >= 90:
    passed = True
    print('Your grade is: A')
elif grade <= 89 and grade >= 80:
    passed = True
    print('Your grade is: B')
elif grade <= 79 and grade >= 70:
    passed = True
    print('Your grade is: C')
elif grade <= 69 and grade >= 60:
    passed = False
    print('Your grade is: D ')
elif grade < 60:
    passed = False
    print('Your grade is: F ')
else:
    print('Unfortunately, you did not pass the class')