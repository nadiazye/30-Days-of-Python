# Day 11 out of 30 Days of Python Challenge
#=======================================================================================================================
#Functions
#This section focuses on custom functions

#Defining a Function
#A function is a reusable block of code or programming statements designed to perform a certain task. To define or
# declare a function, Python provides the def keyword

#The following is the syntax for defining a function. The function block of code is executed only if the function is
# called or invoked

#Declaring and Calling a Function
#When we make a function, we call it declaring a function. When we start using it, we call it calling or invoking a
# function. Functions can be declared with or without parameters.
"""syntax:
Declaring a function:
def function_name():
    code
    code
Calling a function:
function_name()"""

#Function without Parameters
#A function can be declared without parameters
def generate_full_name ():
    first_name = 'Nadia'
    last_name = 'Rodriguez'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name() #Calling the function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

#Function Returning a Value:
#Functions return values using the return statement. If a function has no return statement, it returns None.

#We are going to rewrite the above and use return.
def generate_full_name ():
    first_name = 'Nadia'
    last_name = 'Rodriguez'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

#Function with Parameters
#In a function we can pass different data types (number, string, boolean, list, tuple, dictionary, or set) as parameters
#Single Parameter: If our function takes a parameter we should call our function with an argument
"""syntax:
#Declaring a function:
def function_name(parameter):
    code
    code
#Calling a function:
print(function_name(argument))"""

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Nadia'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range (n+1):
        total += i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Two parameters: A function may or may not have a parameter or parameters. A function may also have two or more parameters.
#If our function takes parameters we should call it with arguments
"""syntax:
#Declaring a function:
def function_name(para1, para2):
    code
    code
Calling a function
print(function_name(argument1, argument2))"""

def generate_full_name(first_name,last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Nadia', 'Rodriguez'))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
pprint("Sum of two numbers: ", sum_two_numbers(10, 20))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity) + ' N' #the value has to be changed to a string first
    return weight
print ("Weight of an object in Newtons: ", weight_of_object(100, 9.81))

#Passing Arguments with Key and Value
#If we pass the arguments with key and value, the order of the arguments does not matter
"""syntax:
#Declaring a function:
def function_name(para1, para2):
    code
    code
#Calling a function
print(function_name(para1 = 'John', para2 = 'Smith')) #order of arguments does not matter here"""

#Function Returning a Value Pt.2
#If we do not return a value with a function, then our function is returning None by default. To return a value with a
#function we use the keyword return followed by the variable we are returning. We can return any kind of data types from a function

#Returning a String:
def print_name(firstname):
    print(firstname)
print_name('John')

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print_full_name( 'John', 'Smith')
#-----------------------------------------------------------------------------------------------------------------------

#Returning a number:
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(10, 20))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2021, 1819))
#-----------------------------------------------------------------------------------------------------------------------

#Returning a boolean
def is_even (n):
    if n % 2 == 0:
        return True  #a return stops further execution of the function, similar to a break
    return False
print(is_even(10))
print(is_even(7))
#-----------------------------------------------------------------------------------------------------------------------

#Returning a list
def find_even_numbers(n):
    even = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)
    return even
print(find_even_numbers(10))
print(find_even_numbers(7))

#Function with Default Parameters
#Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling
# the function, their default values will be used
"""syntax:
#Declaring a function:
def function_name(param = value):
    code
    code
#Calling a function:
function_name()
function_name(arg)"""

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Nadia'))