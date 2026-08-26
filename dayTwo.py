#Day 2 out of 30 Days of Python Challenge
#=======================================================================================================================

#going over pythons built-in functions

print('Hello World') #prints the text value of Hello World
len('Hello World')
print(len('Hello World')) #prints the number of characters including spaces
type('Hello World') #checks the data type
str(10) #converts number to string
float(10) #converts integer to decimal
input('Enter your name:') #takes user input

'''There is a list of Python keywords that you cannot use to declare variables or functions
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except
finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield'''

min(20,30,40,50) #gives the min value in list
max(20,30,40,50) #gives the max value in list
min([20,30,40,50]) #takes the list as an argument and returns min
max([20,30,40,50])  #takes list as an argument and returns max
sum([1,2,3,4,5]) #takes list as an argument and returns the sum

'''Python Variable Name Rules
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha numeric characters and underscores
variable names are case sensitive
Python developers tend to use snake case (snake_case) ex. first_name, persons_skills, number_of_students'''

#Multiple variables can also be declared in one line: Example below

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#You can get user input by using the input() built-in function, example below
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

#Check Data types: To check the data type of certain data/variable we use the type, example below
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int

# Printing out types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

'''Casting is converting one data type to another data type, when we do arithmetic operations string numbers should be 
first converted to a string, examples below '''

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
#print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

#======================================================================================================================
#Day 2 Exercises:
#Exercises Level One

first_name = 'Nadia'
last_name = 'Rodriguez'
full_name = first_name + last_name
country = 'USA'
city = 'Miami'
age = 22
current_year = 2026
is_married = False
is_true = True
is_light_on = True
name, family_name, birth_year, is_single = 'Nadia', 'Rodriguez', 2003, False

print(name, family_name, birth_year, is_single)
#-----------------------------------------------------------------------------------------------------------------------
#Exercises Level Two
print(type(name), type(family_name), type(birth_year), type(is_single))
print(len(name))
print(len(family_name))
num_one, num_two = 5,4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)
#-----------------------------------------------------------------------------------------------------------------------
radius = 30
pi = 3.14
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius

print(area_of_circle)
print(circum_of_circle)