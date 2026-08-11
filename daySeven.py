# Day 7 out of 30 Days of Python Challenge
#=======================================================================================================================
#Sets
"""Set is a collection of items. The math definition of a set can be applied also in Python. Set is a collection of
unordered and un-indexed distinct elements. In python, set is used to store unique items, and it is possible to find
the union, intersection, difference, symmetric difference, subset, super set, and disjoint set among sets."""
from dayFive import vegetables

#Creating a Set
#To creat an empty set, we use the set() function. Empty curly brackets {} will create a dictionary.
#Creating an empty set
#syntax : st = set()

#Creating a set with initial items
#Syntax: st = {'item1', 'item2', 'item3'}
    #Ex: fruits = {'banana','orange','mango'}

#Getting a Set's Length
#We use the len() method to find the length of a set
'''syntax:
st = {'item1', 'item2', 'item3'}
len(st)'''

items = {'item1', 'item2', 'item3'}
len(items)

#Accessing Items in a Set
#We use loops to access items, go to day 10 to see more

#Checking an Item
#To check if an item exist in a list we use in membership operator
'''syntax:
st = {'item1', 'item2', 'item3'}
print("Does set st contain item3?", 'item3' in st) (Does set st contain item3? True) '''

items = {'item1', 'item2', 'item3'}
print('item1' in items)

#Adding Items to a Set
#Once a set is created we cannot change any items, and we can also add additional items
    #Add one item using add()
"""syntax:
st = {'item1', 'item2', 'item3'}
st.add('item4')"""

fruits = {'apple', 'banana', 'orange'}
fruits.add('lime')

    #Add multiple items using update(), it allows to add multiple items to a set, and takes a list argument
"""syntax:
st = {item1, item2, item3}
st.update([item4, item5])"""

fruits = {'apple', 'banana', 'orange'}
vegetables = ('tomato', 'potato', 'cabbage')
fruits.update(vegetables)

#Removing Items from a Set
#We can remove an item from a set using remove() method. If the item is not found remove() will raise errors
#However the discard method will not raise errors
"""syntax:
st = {item1, item2, item3}
st.remove('item2')"""

#The pop() methods remove a random item from a list, and it returns the removed item.
fruits = {'apple', 'banana', 'orange'}
fruits.pop() #removes a random item
#if we are interested in what was removed
removed_item = fruits.pop()

#Clearing Items in a Set
#If we want to clear or empty the set we use the clear method
"""syntax:
fruits = {'apple', 'banana', 'orange'}
fruits.clear()"""

#Deleting a Set
#If we want to delete the set itself, we use the del operator
"""syntax:
st = {'item1', 'item2', 'item3'}
del st"""

fruits = {'apple', 'banana', 'orange'}
del fruits

#Converting List to Set
#We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved
"""syntax:
lst = ['item1', 'item2', 'item3']
st = set(lst)"""

#Joining Sets
#We can join two sets using the union() or update() method or | symbol
#Union, this method returns a new set
"""syntax:
st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st3 = st.1union(st2)"""

fruits = {'apple', 'banana', 'orange'}
vegetables = {'tomato', 'potato', 'cabbage'}
print(fruits.union(vegetables))

#Update, this method inserts a set into a given set
"""syntax:
st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st3 = st.1update(st2)"""

fruits = {'apple', 'banana', 'orange'}
vegetables = {'tomato', 'potato', 'cabbage'}
fruits.update(vegetables)
print(fruits)

#Finding Intersection Items
#Intersection returns a set of items which are both the sets or using & symbol
"""syntax:
st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st1.intersection(st2)"""

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {2,4,6,8,10}
whole_numbers.intersection(even_numbers)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon

#Checking Subset and Super Set
#A set can be a subset or superset of other sets:
#Subset: issubset()
#Super set: issuperset

