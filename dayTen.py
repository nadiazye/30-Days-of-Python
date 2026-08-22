# Day 10 out of 30 Days of Python Challenge
#=======================================================================================================================
#Loops
#Loops are made to handle repetitive tasks, in Python we have two types of loops:
#while loop and for loop

#While Loop
#the word while is of course used for the while loop, it is used to execute a block of statements repeatedly until a
#given condition is satisfied
#When the condition becomes false, the lines of code after the loop will continue to be executed
"""syntax:
while condition:
    code goes here"""

count = 0
while count < 5:
    print(count)
    count = count + 1
#this would print from 0 to 4
#the condition would become false once the count is 5. That is when the loop stops.

#If we would like to run a block of code once the condition is false, then we use else
"""syntax:
while condition:
    code goes here
else:
    code goes here"""

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
#It will become false once the count is 5, therefore executing the else statement.

#Break and Continue
#Break: we use break when we like to get out of or stop the loop
"""Syntax:
while condition:
    code goes here
    if another_condition:
        break"""
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

#with the continue statement we can skip the current iteration, and continue with the next:
"""syntax:
while condition:
    code goes here
    if another_condition:
        continue"""

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

#For Loop
#A for keyword is used to make a for loop, similar to other programs aside from some syntax differences
#Loop is used for iterating over a sequence (like list, tuple, dictionary, set, or string)
#-----------------------------------------------------------------------------------------------------------------------
#Using For loop in a list:
"""syntax:
for iterator in lst:
    code goes here"""

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: #number is temporary name to refer to the list's items, valid only inside this loop
    print(number)
#-----------------------------------------------------------------------------------------------------------------------
#Using For loop on string:
"""syntax:
for iterator in string:
    code goes here"""

langauge = 'Python'
for letter in langauge:
    print(letter)

"""for i in range(len(langauge)):
    print(language[i]) """
#-----------------------------------------------------------------------------------------------------------------------
#Using For loop on tuple
"""syntax:
for iterator in tpl:
    code goes here"""

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
#-----------------------------------------------------------------------------------------------------------------------
#For loop with dictionary Looping through a dictionary gives you the key of the dictionary
"""syntax:
for iterator in dct:
    code goes here"""

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 21,
    'country': 'Finland',
    'is_cool': False,
    'skills': ['Human', 'Feelings', 'Reading', 'Living'],
    'address':{
        'street': 'Regular Man Street',
        'city': 'Metropolis',
}
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)
#-----------------------------------------------------------------------------------------------------------------------
#Using For Loop in set:
"""syntax:
for iterator in st:
    code goes here"""

it_companies = {'Facebook', 'Twitter', 'Instagram'}
for company in it_companies:
    print(company)
#-----------------------------------------------------------------------------------------------------------------------
#Break and Continue - Pt.2
"""syntax:
for iterator in sequence:
    code goes here
    if condition:
        break"""

#Continue: we use continue when we want to skip some of the steps in the iteration of the loop
"""syntax:
for iterator in sequence:
    code goes here
    if condition:
       continue"""

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be ", number + 1) if number != 5 else print("loop's end")
#for shorthand conditions need both if and else statements
print('outside the loop')

#In the example above, if the number equals 3, the step after the condition (but inside the loop) is skipped and the
#execution of the loop continues if there are any iterations left

#The Range Function:
#The range() function is used to return a list of numbers. The range(start, end, step) takes three parameters: starting,
# ending and increment. By default, it starts from 0 and the increment is 1. The range sequence needs at least 1 argument
#(end). Creating sequences using range:
lst = list(range(11))
print(lst) #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1,11)) #2 arguments indicate the start and end of the sequence, step set to default 1
print(st) #output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11, 2))
print(lst) #output: [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #output: {0, 2, 4, 6, 8, 10}

#for backward from start to end
lst = list(range(11,0, -2))
print(lst) # output: [11, 9, 7, 5, 3, 1]

"""syntax:
for iterator in range(start, end, step):"""

for number in range(11):
    print(number) #prints 0 to 10, not including 11

#Nested For Loop:
#We can write loops inside a loop
"""syntax:
for x in y:
    for t in x:
        print(t)"""

person = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 21,
        'country': 'Finland',
        'is_cool': False,
        'skills': ['Human', 'Feelings', 'Reading', 'Living'],
          'address':{
              'street': 'Regular Man Street',
              'city': 'Metropolis',
          }
 }
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#For Else
#If we want to execute some message when the loop ends, we use else
"""syntax:
for iterator in range(start, end, step):
    do something
else:
     print('The loop ended')"""

for number in range(11):
    print(number) # prints 0 to 10, not including 11
else:
    print('The loop stops at ', number)

#Pass
#In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the
# word pass to avoid errors, it can also be used a placeholder for future statements

#ex:
for number in range(6):
    pass
print("-----------------------------------------------------------------------------------------------------------------")
#Exercises:
#Level 1:

#1. Iterate 0 to 10 using for loop, do the same using while loop.
    #for loop
count_up = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in count_up:
    print(number)

print("----------------")

    #while loop
count = 0
while count < 11:
    print(count)
    count = count + 1
print("----------------")
#2. Iterate 10 to 0 using for loop, do the same using while loop.
    #for loop
count_down = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for number in count_down:
    print(number)

print("----------------")
    #while loop
count = 10

while count > -1:
    print(count)
    count = count - 1
print("----------------")

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######

hashtag_text = "#"
print(hashtag_text)

while len(hashtag_text) < 7:

    hashtag_text = hashtag_text + "#"
    print(hashtag_text)

print("----------------")

#4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for row in range(8):
    hashtag = " "
    for column in range(8):
        hashtag += "# "
    print(hashtag)

print("---------------------")

#trying again but for it to be all within one loop:
for row in range(8):
    print("# " * 8)

print("---------------")

#5. Print the following pattern:
"""0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100"""

for number in range(11):
    product = number ** 2
    print (str(number) + " x " + str(number) + " = " + str(product))

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.


#7. Use for loop to iterate from 0 to 100 and print only even numbers

#8. Use for loop to iterate from 0 to 100 and print only odd numbers

#-----------------------------------------------------------------------------------------------------------------------
#Level 2:
#9. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
        #The sum of all numbers is 5050.

#10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
        #The sum of all evens is 2550. And the sum of all odds is 2500.
#-----------------------------------------------------------------------------------------------------------------------
#Level 3:
#11. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
#12. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
#13. Go to the data folder and use the countries_data.py file.
    #13a. What are the total number of languages in the data
    #13b. Find the ten most spoken languages from the data
    #13c. Find the 10 most populated countries in the world


