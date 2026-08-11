# Day 6 out of 30 Days of Python Challenge
#=======================================================================================================================
#Tuples
"""A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written
with round brackets, {}. Once a tuple is created, we cannot change its values. We cannot use add, insert, or remove
methods in a tuple because it is not modifiable (mutable).
Unlike list, a tuple has few methods. Methods related to tuples:
tuple(): to create an empty tuple
count() to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
+ operator: to join two or more tuples to create a new tuple"""

#Creating a Tuple
#Empty tuple: creating an empty tuple
""" syntax: 
      empty_tuple = ()
      or using the tuple constructor
      empty_tuple = tuple()"""
#Tuple with initial values
tpl = ('item1','item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

#Tuple Length
    #We use len() method to get the length of a tuple
"""syntax:
    tpl = ('item1', 'item2', 'item3')
    len(tpl)"""

#Accessing Tuple Items
#Positive Indexing Similar to the list data type we use positive or negative indexing to access tuple items
''' syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]'''

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits)-1
last_fruit = fruits[last_index]

#Negative indexing means beginning from the end, -1 refers to the last item and so on.
#The negative of the list/tuple length refers to the first item.
'''syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[-4]
second_item = tpl[-3]'''

#Slicing Tuples
#We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return
#value will be a new tuple with the specified items.

#Range of Positive Indexes
'''syntax
    tpl = ('item1', 'item2', 'item3')
    all_items = tpl[0:4]
    all_items = [tpl[0:]
    middle_two_items = tpl[1:3] (doesn't include the item at index 3'''
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]

#Range of Negative Indexes
'''# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)'''

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

#Changing Tuples to Lists
#We can change tuples to lists and lists tu tuples. Tuple is immutable if we want to modify a tuple we should change it to a list
'''syntax
tpl = ('item1', 'item2', 'item3')
lst = list(tpl)'''

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
fruits = tuple(fruits)
print(fruits)

#Checking an Item in a Tuple
#We can check if an item exists or not in a tuple using in, which returns a boolean
'''syntax
tpl = ('item1', 'item2', 'item3')
'item2' in tpl (would return true)'''

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) #would return true
print('apple' in fruits) #would return false

#Joining Tuples
#We can join two or more tuples using + operator
'''syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2'''

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_veggies = fruits + vegetables
print(fruits_and_veggies)

#Deleting Tuples
#it is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del
'''syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1'''

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
#=======================================================================================================================
#Exercises: Level 1
#-----------------------------------------------------------------------------------------------------------------------
#1. Create an empty tuple
empty_tuple = ()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother_names = ('Sean', 'Enzo')
sister_names = ('Jazlyn', 'Nadia')

print(brother_names)
print(sister_names)

#3. Join brothers and sisters tuples and assign it to siblings
siblings = brother_names + sister_names

print(siblings)

#4. How many siblings do you have?
print(len(siblings))

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)

siblings.append('Zulie')
siblings.append('Jose')

family_members = siblings
print(family_members)

#Exercises: Level 2
#-----------------------------------------------------------------------------------------------------------------------
#6. Unpack siblings and parents from family_members

#7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
animals = ('Pig', 'Cow', 'Chicken')

food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

#8. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)

#9. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items_only = food_stuff_lt[4:6]

print(middle_items_only)

#10. Slice out the first three items and the last three items from food_stuff_lt list
first_three_gone = food_stuff_lt[0:3]
last_three_gone = food_stuff_lt[-3:]
print(first_three_gone)
print(last_three_gone)

#11. Delete the food_stuff_tp tuple completely
del food_stuff_tp

#print(food_stuff_tp) #should return error, it does

#12. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#12a. Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

#12b. Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
