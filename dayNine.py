# Day 9 out of 30 Days of Python Challenge
#=======================================================================================================================
#Conditionals
#By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so,
# the sequential flow of execution can be altered in two ways:
#Conditional execution: a block of one or more statements will be executed if a certain expression is true
#Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true

#If Condition:
#In python other languages, the key word if is used to check if a condition is true and to execute the block code
#MUST remember the indentation after the colon
"""syntax:
if condition:
    this part of code runs for truthy conditions"""

#Example 1:
a = 3
if a > 0:
    print('A is a positive number')
#Obviously, 3 is greater than 0 and since a = 3, the condition block was true and executed
#However, if the condition was false then we wouldn't see the result

#If else
#If the condition is true the first block will be executed, if not the else condition will run
"""syntax:
if condition:
    this part of code runs for truthy conditions
else:
    this part of code runs for false conditions"""

#Example 2:
a =3
if a > 0:
    print('A is a negative number')
else:
    print('A is a positive number')
#The condition above proves false, therefore the else block was execution.

#If Elif Else
#Programming is full of conditions, we use elif when we have multiple conditions
"""syntax:
if condition:
    code
elif condition:
    code
else:
    code"""

#Example 3
a = 0
if a > 0:
    print('A is a positive number.')
elif a < 0:
    print('A is a negative number.')
else:
    print('A is a zero.')

#Short Hand:
"""syntax:
code if condition else code"""

#Example 4:
a = 3
print('A is positive') if a > 0 else print('A is negative') #first condition is met

#Nested Conditions
# Conditions can be nested
"""syntax:
if condition:
     code
     if condition:
     code"""

#Example 5:
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is an even and positive integer.')
    else:
        print('A is a positive integer.')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative integer.')

#We can avoid overwriting nested loops if we use the and operator

#If Condition and Logical Operators
"""syntax:
if condition and condition: 
    code"""

#Example 6:
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer.')
elif a > 0 and a % 2 !=0:
    print('A is a positive integer.')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative integer.')

#If and Or Logical Operators
"""syntax:
if condition  or condition: 
    code"""

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access is granted')
else:
    print('Access is denied')

#=======================================================================================================================
#Exercises:
#Level 1:

#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.

user_age = (input('Please enter your age: '))
driving_math = 16 - int(user_age)
if int(user_age) >= 16:
    print("You're able to drive! Where's your license?")
elif int(user_age) < 16:
    print("You need " + str(driving_math) + " more years until you can drive.")
else:
    print("That's not a real age!")
    """ Output:
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive. """

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)?
    # Use input(“Enter your age: ”) to get the age as input.
    # You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
    # and a custom text if my_age = your_age.

"""Output:
Enter your age: 30
You are 5 years older than me."""

#3. Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = input("Put the number you want A to be: ")
b = input("Put the number you want B to be: ")

if int(a) > int(b):
    print(str(a) + " is greater than " + str(b))
elif int(a) < int(b):
    print(str(a) + " is less than " + str(b))
else:
    print(str(a) + " is equal to " + str(b))

"""Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3"""
#-----------------------------------------------------------------------------------------------------------------------
#Level 2:

#4. Write a code which gives grade to students according to theirs scores:
""" 90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F """
grade_input = (input("Please enter your grade: "))

if 60 <= int(grade_input) <= 69:
    print("Your grade is a D!")
elif 70 <= int(grade_input) <= 79:
    print("Your grade is a C!")
elif 80 <= int(grade_input) <= 89:
    print("Your grade is a B!")
elif 90 <= int(grade_input) <= 100:
    print("Your grade is an A!")
elif int(grade_input) <= 59:
    print("Your grade is a F!")
else:
    print("Error")

#5. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer

user_month = input("Please enter your month: ")

if user_month in ['December','January','February']:
    print('Your season is Winter')
elif user_month in ['March', 'April', 'May']:
    print('Your season is Spring')
elif user_month in ['June','July', 'August']:
    print('Your season is Summer')
elif user_month in ['September', 'October', 'November']:
    print('Your season is Autumn')
else:
    print('Your month is nonexistent.')

#6. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

#6 (continued). If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')

fruits_input = input("Please enter a fruit: ")

if fruits_input in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruits_input)
    print(fruits)
#-----------------------------------------------------------------------------------------------------------------------
#Level 3:
    person={
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
"""#7
 7a. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 7b. Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 7c. If a person skills has only JavaScript and React, print('He is a front end developer'), 
    if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
    if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
        - for more accurate results more conditions can be nested!
 7d. If the person is married and if he lives in Finland, print the information in the following format:"""
# Asabeneh Yetayeh lives in Finland. He is married.

print("Let's check this person's profile!")

if 'skills' in person:
    print(person['skills'][2])

if 'Python' in 'skills':
    print(person['skills'])

