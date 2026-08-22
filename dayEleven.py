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
    pie = 3.14
    area = pie * r ** 2
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

def generate_full_name(first_name = 'Nadia', last_name = 'Rodriguez'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Nadia', 'Rodriguez'))

def calculate_age (birth_year, current_year = 2026):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1800))

def weight_of_object(mass, gravity = 9.81):
    weight = str(mass * gravity) + ' N'
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100))
print(weight_of_object(100, 1.62))

#Arbitrary Number of Arguments
#If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary
#number of arguments by adding * before the parameter name
"""syntax:
#Declaring a function:
def: function_name(*args)"
    code
    code
#Calling a function:    
function_name(param1, param2, param3, ...)"""

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num #this is the same as total = total + num
    return total
print(sum_all_nums(2, 3, 5))

#Default and Arbitrary Number of Parameters in Functions:
def generate_groups (team, *args):
    print (team)
    for i in args:
        print(i)
generate_groups('Team 1', 'Nadia', 'Liz', 'Asabeneh')

#Dictionary unpacking:
#You can call a function which has named arguments using a dictionary with matching key names. You do so using **
#Define a function that takes two arguments: 'name' and 'location'
def greet(name,location):
    #Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

#Call the function using keyword arguments
greet(name = "Alice", location = "New York")

#Call the function using dictionary unpacking
greet(**my_dict)
#The ** operator unpacks the dictionary, passing its key-value pairs as keyword arguments to the function
#Output: Hi there Alice how is the weather in New York

#Arbitrary Number of Named Arguments
#You can also define a function to accept an arbitrary number of named arguments
def arbitrary_named_args(*args):
    print("I received an arbitrary number of arguments, totaling, ", len(args))
    print("They are provided as a dictionary in my function: ", type(args))
    print("Let's print them: ")
    for k, v in args.items():
        print(" # key:", k, "value:", v)
#Generally a good rule of thumb to avoid doing this unless it is required as it makes it harder to understand what this
# function accepts and does

#Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number(n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))
#-----------------------------------------------------------------------------------------------------------------------
#Exercises:
#Level 1:

#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not, do give a reasonable feedback.

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

#5. Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.

#6. Write a function called calculate_slope which return the slope of a linear equation

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

#8. Declare a function named print_list. It takes a list as a parameter, and it prints out each element of the list.

#9. Declare a function named reverse_list.
# It takes an array as a parameter, and it returns the reverse of the array (use loops).
"""
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"] """

#10. Declare a function named capitalize_list_items. It takes list as a parameter and ir returns a capitalized
# list of items

#11. Declare a function named add_iem. It takes a list and an item parameters. It returns a list with the item
# added at the end.
"""
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5] """

#12. Declare a function named remove_item. It takes a list an items parameters. It returns a list with the item
# removed from it
"""
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9] """

#13. Declare a function named sum_of_numbers. It takes a number parameter, and it adds all the numbers in that range
"""
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))"""

#14. Declare a function named sum_of_odds. It takes a number parameter, and it adds all the odd numbers in that range.

#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
#-----------------------------------------------------------------------------------------------------------------------
#Level 2:
#16. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number
# of evens and odds in the number.
"""
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
"""

#17. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

#18. Call your function is_empty, it takes a parameter and it checks if it is empty or not

#19. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode,
# calculate_range, calculate_variance, calculate_std (standard deviation).

#20. Write a function called greet which takes a default argument, name. If no argument is supplied it
# should print "Hello, Guest!", otherwise it should greet the person by name.
"""    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!" """

#21. Create a function called show_args to take an arbitrary number of named arguments and print their names and values
"""
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny"""

#-----------------------------------------------------------------------------------------------------------------------
#Level 3:
#22. Write a function called is_prime, which checks if a number is prime.

#23. Write a functions which checks if all items are unique in the list.

#24. Write a function which checks if all the items of the list are of the same data type.

#25. Write a function which check if provided variable is a valid python variable

#26. Go to the data folder and access the countries-data.py file.
    #26a. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken
     # languages in the world in descending order
    #26b. Create a function called the most_populated_countries. It should return 10 or 20 most populated countries
        # in descending order.

#-----------------------------------------------------------------------------------------------------------------------