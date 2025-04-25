# Exercise: Day 3
# Declare your age as integer variable
age = int(32)
print(age)
# Declare your height as a float variable
height = float(175.26)
print(height)
# Declare a variable that store a complex number
compl_num = 1 + 1j
print(compl_num)
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input('Enter the base: '))
height = int(input('Enter the height: '))
area = 0.5 * base * height
print(area)
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input('Enter length of side a: '))
side_b = int(input('Enter length of side b: '))
side_c = int(input('Enter length of side c: '))
perimeter = side_a + side_b + side_c
print(perimeter)
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter length of rectangle: '))
width = int(input('Enter width of rectangle: '))
area = length * width
print(area)
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
pi = math.pi
radius = float(input('Enter radius of circle: '))
area = pi * radius * radius
circum = 2 * pi * radius
print(f" The area of the circle is {area:,.2f} and the circumference is {circum:,.2f}")
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_intercept = (0+2)/2
print(x_intercept)
y_intercept = (2*0) - 2
print(y_intercept)
print(f"The x-intercept is (1,0) and the y-intercept is (0,-2)")
slope_eight = (-2 - 0)/(0 - 1)
print(f"The slope is {slope_eight}")
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope_nine = (10 - 2)/(6 - 2)
print(f"The slope for (2, 2) and (6, 10) is {slope_nine}")
# Compare the slopes in tasks 8 and 9.
print(f"The slope of task 8 is {slope_eight} and the slope of task 9 is {slope_nine}")
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(10):
    y = (x - 3) * (x - 3)
    if y == 0:
        print(f"y is zero when x is {x}")
    else:
        print(f"{x}")
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_len = len('python')
dragon_len = len('dragon')
print(python_len == dragon_len)
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'dragon':
    print('On is in the word python and dragon')
else:
    print('On is not in the word python and dragon')
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if 'jargon' in 'I hope this course is not full of jargon.':
    print('Jargon is in the sentence.')
else:
    print('Jargon is not in the sentence')
# There is no 'on' in both dragon and python
# Find the length of the text python and convert the value to float and convert it to string
python_len = float(len('python'))
print(python_len)
python_len = str(python_len)
print(python_len)
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python? Use the modulus operator
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
y = 7 % 3
if y == 2.7: print('True') 
else: print('False')
# Check if type of '10' is equal to type of 10
if type(10) == type('10'): print('True')
else: print('False')
# Check if int('9.8') is equal to 10
if int(9.8) == 10: print('True')
else: print('False')
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('How many hours did you work today? '))
rate_hr = float(input('What is your rate per hour? '))
pay = (hours * rate_hr)
print(f"Your pay for today is ${pay:,.2f}")
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
age = int(input('Enter your age: '))
left = 100 - age
sec = left * 365 * 24 * 60 
print(f"A person at the age of {age} has {sec} seconds left before reaching 100 years old.")
# Write a Python script that displays the following table