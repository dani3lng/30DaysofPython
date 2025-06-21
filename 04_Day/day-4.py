# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

string_one = 'Thirty'
string_two = 'Days'
string_three = 'Of'
string_four = 'Python'
space = ' '
sentence_one = string_one + space + string_two + space + string_three + space + string_four
print(sentence_one)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

string_one = 'coding'
string_two = 'for'
string_three = 'all'
space = ' '
sentence_two = string_one + space + string_two + space + string_three
print(sentence_two.title())

# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().

company = sentence_two
print(company.title())

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

string_five = 'Coding For All'
print(string_five.capitalize())
print(string_five.title())
print(string_five.swapcase())

# Cut(slice) out the first word of Coding For All string.

string_five_slice = string_five[6:]

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(string_five.index('Coding'))
print(string_five.find('Coding'))