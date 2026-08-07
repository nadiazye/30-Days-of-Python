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
#from traceback import print_stack

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
    #Positive indexing = we can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list
        #(default values for start = 0, end = len(lst) - 1 (last item), step = 1)
fruits_ver3 = ['banana', 'orange', ' mango', ' lemon']
all_fruits = fruits_ver3[0:4]

all_fruits = fruits_ver3[0:] #if we don't put where to stop then it continues and shows the rest
orange_and_mango = fruits_ver3[1:3]
orange_mango_lemon = fruits_ver3[1:]
orange_and_lemon = fruits_ver3[::2] #here used is a 3rd argument, it will take every second item

#prints of above
print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)

#Negative Indexing - we can specify a range of negative indexes by specifying the start,
#end and step, the return value be a new list
        #using fruits_ver3 again
all_fruits_ver2 = fruits_ver3[-4:] #returns all the indexes
orange_and_mango_2 = fruits_ver3[-4:] #does not include the last index
orange_mango_lemon_2 = fruits_ver3[-3:] #this prints the result starting from -3 to the end
reverse_fruits = fruits[::-1]  #a negative step will take the list in reverse order

#printing the above
print(all_fruits_ver2)
print(orange_and_mango_2)
print(orange_mango_lemon_2)
print(reverse_fruits)

#Modifying Lists
    #list is a mutable or modifiable ordered collection of items
#using the fruits variable/list from above
fruits[0] = 'avocado'
print(fruits)

fruits[1] = 'apple'
print(fruits)

last_index_2 = len(fruits) - 1

fruits[last_index_2] = 'lime'
print(fruits)

#Checking Items in a List
    #checking an item if it is a member of a list using in operator
#using fruits variable/list from above
does_exist = 'banana' in fruits
print(does_exist)

does_exist = 'lime' in fruits
print(does_exist)

#Adding Items to a List
#to add item to the end of an existing list we use the method append()
 #the syntax
 '''lst = list()
    lst.append(item)'''
#using fruits variable/list from above
fruits.append('apple')
print(fruits)

fruits.append('lime')
print(fruits)

#Inserting Items into a List
#We can use insert() method to insert a single item at a specified index in a list.
#This will shift the other items to the right. The insert() methods takes two arguments: index and an item to start
   #syntax
'''   lst = ['item1','item2']
      lst.insert(index,item)'''

#once more using the fruits variable
fruits.insert(2, 'apple')
print(fruits)

fruits.insert(3, 'lime')
print(fruits)

#Removing Item from a List
#the remove method removes a specified item from a list
''' syntax:
lst = [item1,item2]
lst.remove(item)'''

#using fruits variable once more
fruits.remove('banana')
print(fruits)

fruits.remove('lemon')

#Removing Items Using Pop
'''syntax
lst = [item1,item2]
lst.pop() the last item
lst.pop(index)
'''

#using fruits variable
fruits.op() #should get rid of the last index
print(fruits)

fruits.pop(0) #should get rid of the first index
print(fruits)

#Removing Items Using Del
#The del keyword removes the specified index and it can also be used to delete items
# within index range. It can also delete the list completely
'''syntax
lst = [item1,item2]
del lst[index] #to delete one item 
del lst #to delete list completely'''

del fruits[0]
print(fruits)

del fruits[1]
print(fruits)

del fruits[1:3] #this deletes items between the given indexes, does not delete the item with index 3
print(fruits)

del fruits
print(fruits) #This should give an error as the list no longer exists

#Clearing List Items
#The clear() method empties the list:
'''syntax
lst = [item1,item2]
lst.clear()'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.clear()
print(fruits) #output [ ]

#Copying a List
'''It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1
Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1
But there are lots of cases in which we do not like to modify the original instead we like to have a different
copy. Thus, the copy() function'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits_copy = fruits.copy()
print(fruits_copy)

#Joining Lists
#There are several ways to join or concatenate, two or more lists in Python
#Using the plus operator (+)
  #syntax lst3 = lst2 + lst1

positive_num = [1, 2, 3, 4, 5]
zero = [0]
negative_num = [-5, -4, -3, -2, -1]

integers = negative_num + zero + positive_num
print(integers)

fruits_list = ['banana', 'orange', 'mango', 'lemon', 'apple']
vegetables_list = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veggies = fruits_list + vegetables_list
print(fruits_and_veggies)

#Joining using extend() method
#The extend() method allows to append list in a list

'''syntax
list1 = [item1, item2]
list2 = [item 3, item 4, item 5]
list1.extend(list2)'''

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers: ', num1)
negative_num = [-5, -4, -3, -2, -1]
positive_num = [1, 2, 3, 4, 5]
zero = [0]

negative_num.extend(zero)
negative_numbers.extend(positive_num)
print('Integers: ', negative_num)

fruits_list.extend(vegetables_list)
print('Fruits and veggies: ', fruits_list)

#Counting Items in a List
#The count() methods returns the number of times and item appears in a list:
'''syntax
lst = ['item1', 'item2']
lst.count(item)'''

fruits_count = ['banana', 'orange', 'mango', 'lemon']
print(fruits_count.count('orange'))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

#Finding Index of an Item
#the index() method returns the index of an item in the list:
'''
lst = ['item1', 'item2']
lst.index(item)'''

fruits_index = ['banana', 'orange', 'mango', 'lemon']
print(fruits_index.index('orange'))

ages_index = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages_index.index(24))

#Reversing a List
#the reverse() method reverses the order of a list
'''syntax
lst = ['item1', 'item2']
lst.reverse()'''

fruits_reverse = ['banana', 'orange', 'mango', 'lemon', 'apple']
fruit_reverse.reverse()
print(fruits_reverse)

ages_reverse = [22, 19, 24, 25, 26, 24, 25, 24]
ages_reverse.reverse()
print(ages_reverse)

#Sorting List Items
'''To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list
items in ascending order and modifies the original list
If an argument of sort() method reverse is equal to true, it will arrange the list in descending order'''

#sort(): this method modifies the original list
''' syntax
lst = ['item1', 'item2']
lst.sort() #ascending
lst.sort(reverse=True) #descending'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.sort()
print(fruits)      #sorted in alphabetical order
fruits.sort(reverse=True)
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)

#sorted(): returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
print(sorted(fruits))

#now in reverse
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits = sorted(fruits, reverse=True)
print(fruits)


