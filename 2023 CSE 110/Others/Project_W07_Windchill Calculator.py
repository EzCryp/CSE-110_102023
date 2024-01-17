""""
Author: Ezra Zacarias
Prove: W07_Windchill Calculator
"""
#
print("Welcome to the Wind-chill Calculator!\n")

# create a list
speed = [5,10,15,20,25,30,35,40,45,50,55,60]

# create the function for temperature
def Fahrenheit(w):
    return float(w*(9/5)+32)

# create the function for windchill
def windchill(w, i):
    return float(((35.74) + (0.6215*w) - (35.75*(i**0.16)) + ((0.4275*w)*(i**0.16))))

# create variables and ask the user for inputs
w = float(input("What is the temperature? "))
temp = input("Fahrenheit or Celsius? (F/C) ").upper()

# create if statements depending on the inputs and calculate 
# for Fahrenheit input
if temp == "F":
     for i in speed:
        speed = i
        chill = windchill(w, i)
        # display the windchill value 2 decimal of precision
        print(f"At temperature {w:.1f}, and a wind speed of {i} MPH, the windchill is: {chill:.2f}F")

# if statement for Celsius input
elif  temp == "C":
    celsius = Fahrenheit(w)
    w = celsius
    for i in speed:
        chill = windchill(w, i)

        print(f"At temperature {w:.1f}, and a wind speed of {i} MPH, the windchill is: {chill:.2f}F")
        
else:
    # additional message if wrong input
    print("\nCannot compute, please check requirements and retry. ")
# additional warning message 
print("\nStay safe in that chilly wind and be prepared! ")

