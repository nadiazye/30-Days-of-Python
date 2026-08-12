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
"""# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True"""

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

#Checking the Difference Between Two Sets
#it returns the difference between two sets or using - symbol
"""# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1"""

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python

#Finding Symmetric Difference Between Two Sets
#It returns the symmetric difference between two sets. It means that it returns a set that contains all items from both
#sets, except items that are present in both sets, mathematically: (A\B) U (B\A)
"""# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1"""

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon

#Joining Sets
#If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or
#disjoint using isdisjoint() method
"""# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False"""

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

#=======================================================================================================================
#Exercises:
#Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1. Find the length of the set it_companies
print(len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Nvidia', 'AMD', 'Nokia'])
print(it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

#5. What is the difference between remove and discard
    #Remove raises an error if you try to remove something that is not there, discard doesn't
#it_companies.remove('Twitter')
print(it_companies) #^ does return an error

it_companies.discard('Twitter')
print(it_companies)

#-----------------------------------------------------------------------------------------------------------------------
#Level 2:
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#6. Join A and B
C = A.union(B)
print(C)

#7. Find A intersection B
A.intersection(B)
print(A.intersection(B))

#8. Is A subset of B
print(B.issubset(A))

#9. Are A and B disjoint sets
print(A.isdisjoint(B))

#10. Join A with B and B with A
AB_set = A.union(B)
print(AB_set)

BA_set = B.union(A)
print(BA_set)

#11. What is the symmetric difference between A and B
print(B.symmetric_difference(A))

#12. Delete the sets completely
del A
del B

#-----------------------------------------------------------------------------------------------------------------------
#Level 3:
age = [22, 19, 24, 25, 26, 24, 25, 24]

#13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)

print(len(age_set))
print(len(age))
print('Age list is bigger than the set.')

#14. Explain the difference between the following data types: string, list, tuple and set
print("A string is: any text that is written.")
print("A list is: is a collection which is ordered and changeable, allows duplicate members.")
print("A tuple is: a collection of different data types which is ordered and unchangeable (immutable).")
print("A set is: a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set, "
      "NO duplicates. ")

#15. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.
