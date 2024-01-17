print("Welcome to the wind-chill calculator!\n")

# create a list
speed = [5,10,15,20,25,30,35,40,45,50,55,60]

#Create temperature and windchill function
def Fahrenheit(w):
    return float(w*(9/5)+32)

def windchill(w, i):
    return float(((35.74) + (0.6215*w) - (35.75*(i**0.16)) + ((0.4275*w)*(i**0.16))))

# Set up variables and inputs 

w = float(input("What is the temperature? (#) "))
temp = input("Fahrenheit or Celsius? (F/C) ").upper()

#Create statements depending on the inputs and calculate

if temp == "F":
     for i in speed:
        speed = i
        chill = windchill(w, i)

        print(f"At temperature {w:.1f}, and a wind speed of {i} MPH, the windchill is: {chill:.2f}F")
        
elif  temp == "C":
    celsius = Fahrenheit(w)
    w = celsius
    for i in speed:
        chill = windchill(w, i)

        print(f"At temperature {w:.1f}, and a wind speed of {i} MPH, the windchill is: {chill:.2f}F")
        

else:
    print("Can not compute, please check requirements and retry. ")
        
print("Stay safe in that chilly wind and be prepared! ")