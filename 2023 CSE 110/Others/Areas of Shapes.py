# Create prompt question asking for the length of the square and create an output of the area of that square
import math
len_of_sqr_side = float(input('What is the length of a side of the square? '))
area_of_sqr = len_of_sqr_side ** 2
print (f'The area of the square is: {area_of_sqr: .2f}')

# Create a prompt question asking for the length and width of the rectangle and the output is the area of the rectangle

len_of_rec = float(input('What is the length of rectangle? '))
width_of_rec = float(input('What is the width of the rectangle? '))
area_of_rec = len_of_rec * width_of_rec
print (f'The area of the rectangle is: {area_of_rec: .2f}')


# Create a prompt question asking for the radius of the circle and the output is the area of the circle

rad_of_circ = float(input('What is the radius of the circle? '))
area_of_circ = math.pi * (rad_of_circ ** 2)
print(f'The area of the circle is: { area_of_circ: .2f}')


