# Day 2: 30 Days of python programming

# Exercise: Level 1
# Declare a first name variable and assign a value to it
first_name = 'John'
# Declare a last name variable and assign a value to it
last_name = 'Doe'
# Declare a full name variable and assign a value to it
full_name = 'John Doe'
# Declare a country variable and assign a value to it
country = 'United States'
# Declare a city variable and assign a value to it
city = 'Portland'
# Declare an age variable and assign a value to it
age = 25
# Declare a year variable and assign a value to it
year = 2000
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = True
# Declare multiple variable on one line
full_name, age, city, country, is_married = 'John Doe', '25', 'Portland', 'United States', 'No'
print(full_name, age, city, country, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Exercise: Level 2
# Check the data type of all your variables using type() built-in function
print(type(full_name))
print(type(age))
print(type(city))
print(type(country))
print(type(is_married))
# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
print('Last name has', len(last_name), 'letter while my first name has ', len(first_name), 'letters.')
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
print(num_one)
print(num_two)
# Add num_one and num_two and assign the value to a variable total
num_sum = num_two + num_one
print(num_sum)
# Subtract num_two from num_one and assign the value to a variable diff
num_sub = num_two - num_one
print(num_sub)
# Multiply num_two and num_one and assign the value to a variable product
num_mult = num_two * num_one
print(num_mult)
# Divide num_one by num_two and assign the value to a variable division
num_div = num_two / num_one
print(num_div)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
num_mod = num_two % num_one
print(num_mod)
# Calculate num_one to the power of num_two and assign the value to a variable exp
num_pow = num_one ** num_two
print(num_pow)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
num_floor = num_one // num_two
print(num_floor)
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
import math
pi = math.pi
radius = 30
area_circle = float(pi * (30 ** 2))
print(area_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_circle = float(2 * pi * 30)
print(circum_circle)
# Take radius as user input and calculate the area.
radius = int(input('Enter circle radius:' ))
area_circle = float(pi * (radius ** 2))
print(area_circle)
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
country = input('Country: ')
age = input('Enter age: ')
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')