#Day 5 out of 30 Days of Python Challenge

#Lists
'''
These are four collection data types in Python:
    List: is a collection which is ordered and changeable, allows duplicate members
    Tuple: is a collection which is ordered and unchangeable (immutable), also allows duplicate members
    Set: a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set, NO duplicates
    Dictionary: a collection which is unordered, changeable, and indexed, NO duplicates

A list is a collection of different data types which is ordered and modifiable (mutable). A list can be empty
or it may have different data type items.

How to Create a List:
In Python we can create lists in two ways:
'''

#Using list built-in function
lst = list() #syntax

empty_list = list() #this is an empty list, no items in this
print(len(empty_list)) #should return a 0

#You can also use square brackets, []
#lst = [] #syntax

empty_list = [] #this is an empty list as well
print(len(empty_list)) #should also return 0

#Below are lists with initial values, we can use len() to find the length of the list
fruits = ['banana', 'orange', 'mango', 'lemon'] #list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']  #list of veggies
animal_products = ['milk', ' meat', 'butter', 'yogurt']  #list of animal byproducts
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB'] #list of programs
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] #list of countries

#Printing the lists and their lengths
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animals:', animal_products)
print('Number of animals:', len(animal_products))
print('Web Techs:', web_techs)
print('Number of web programs:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

#Lists can also have items of different data types
lst_again = ['Asabeneh', 250, True, {'country':'Finland', 'city': 'Miami'}]

#Accessing List Items with Using Positive Indexing, a list index starts from 0
    #using the fruits list from before
first_fruit = fruits[0]
print(first_fruit)

second_fruit = fruits[1]
print(second_fruit)

last_fruit = fruits[-1]
print(last_fruit)

last_index = len(fruits) - 1
last_fruit = fruits[last_index]

#Accessing List Items with Using Negative Indexing, neg indexing means starting from the end
#-1 refers to the last item, -2 refers to the second to last term
    #using the list fruit again
back_first_fruit = fruits[-4]
print(back_first_fruit)

back_last_fruit = fruits[-1]
print(back_last_fruit)

back_second_last_fruit = fruits[-2]
print(back_second_last_fruit)

#Unpacking List Items
list_of_items = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = list_of_items
print(first_item)
print(second_item)
print(third_item)
print(rest)

#Example One
fruits_ver2 = ['banana', 'orange', ' mango', ' lemon', 'lime', 'apple']
ver2_first, ver2_second, ver2_third, *rest = fruits_ver2

print(ver2_first) #output should be banana
print(ver2_second) #output should be orange
print(ver2_third) #output should be mango
print(rest) #lemon, lime, apple

#Example Two
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

#Example Three
countries_ver2 = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries_ver2
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#Slicing Items from a List
    #Positive indexing = we ca specify a range of positive indexes by specifying the start, end and step, the return value will be a new list
        #(default values for start = 0, end = len(lst) - 1 (last item), step = 1)
fruits_ver3 = ['banana', 'orange', ' mango', ' lemon']
all_fruits = fruits_ver3[0:4]


