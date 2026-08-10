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
#lst = list()
# lst.append(item)
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
fruits = ['banana', 'orange', 'mango', 'lemon']
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
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop() #should get rid of the last index
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

#del fruits[1]
print(fruits)

del fruits[1:3] #this deletes items between the given indexes, does not delete the item with index 3
print(fruits)

'''del fruits
print(fruits) #This should give an error as the list no longer exists (to which it did) '''

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
negative_num.extend(positive_num)
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
fruits_reverse.reverse()
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
#=======================================================================================================================
print('=================================================================================================================')
#Day 5 Exercises

#1. Declare an empty list
empty_list = []

#2. Declare a list with more than 5 items
multiple_item_list =['item1', 'item2', 'item3', 'item4', 'item5']

#3. Find the length of your list
print(len(multiple_item_list))

#4. Get the first item, the middle item and the last item of the list
multiple_item_list = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item = multiple_item_list[0]
middle_item = multiple_item_list[2]
last_item = multiple_item_list[-1]

print(first_item)
print(middle_item)
print(last_item)

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Nadia', 22, 5.3, 'Single', 'Miami']
print(mixed_data_types)

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[::2])

#10. Print the list after modifying one of the companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

it_companies[0] = 'Nokia'
print(it_companies)

#11. Add an IT company to it_companies
it_companies = ['Nokia', 'Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

it_companies.append('Twitter')
print(it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies = ['Nokia', 'Facebook','Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon', 'Twitter']

it_companies[4] = 'Nvidia'
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ['Nokia', 'Facebook', 'Google', 'Microsoft', 'Nvidia', 'Oracle', 'Amazon', 'Twitter']

#14. Join the it_companies with a string '#;  '
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

join_var = ['#; ']
joined_companies = it_companies + join_var

print(joined_companies)

#15. Check if a certain company exists in the it_companies list.
does_IT_exist = 'Facebook' in it_companies
print(does_IT_exist)

#16. Sort the list using sort() method
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#18. Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

first_three = it_companies[0:3]
print(first_three)

#19. Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

last_three = it_companies[-3:]
print(last_three)

#20. Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

exclude_middle = it_companies[0:2:3]
print(exclude_middle)

#21. Remove the first IT company from the list

#22. Remove the middle IT company or companies from the list

#23. Remove the last IT company from the list

#24. Remove all IT companies from the list

#5. Destroy the IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon']

it_companies.clear()
print(it_companies)

#26. Join the following lists:
''' front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB'] '''

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_dev = front_end + back_end
print(full_dev)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack,
        # then insert Python and SQL after Redux.
full_dev_copy = full_dev.copy()

print(full_dev_copy)
full_dev_copy.insert(5,'Python')
full_dev_copy.insert(6, 'SQL')

print(full_dev_copy)
#28. The following is a list of 10 students ages:
         #ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

#29. Sort the list and find the min and max age
ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[-1]
print(min_age, max_age)

#30. Add the min age and the max age again to the list

#31. Find the median age (one middle item or two middle items divided by two)

#32. Find the average age (sum of all items divided by their number )

#33. Find the range of the ages (max minus min)
range_of_age = max_age - min_age
print(range_of_age)

#34. Compare the value of (min - average) and (max - average), use abs() method

#35. Find the middle country(ies) in the countries list
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia',
    'Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin',
    'Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi',
    'Cabo Verde','Cambodia','Cameroon','Canada','Central African Republic', 'Chad','Chile','China','Colombia','Comoros',
    'Congo, Democratic Republic of the','Congo, Republic of the','Costa Rica',"Côte d'Ivoire",'Croatia','Cuba','Cyprus',
    'Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor-Leste)','Ecuador','Egypt',
    'El Salvador','Equatorial Guinea','Eritrea','Estonia','Eswatini','Ethiopia','Fiji','Finland','France','Gabon',
    'Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti',
    'Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Italy','Jamaica','Japan','Jordan',
    'Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon',
    'Lesotho','Liberia','Libya','Liechtenstein', 'Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives',
    'Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia',
    'Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua',
    'Niger','Nigeria','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine', 'Panama','Papua New Guinea',
    'Paraguay','Peru','Philippines','Poland','Portugal','Puerto Rico', 'Qatar','Romania','Russia','Rwanda',
    'Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe',
    'Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands',
    'Somalia','South Africa','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria',
    'Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu',
    'Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu',
    'Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']

#36. Divide the countries list into two equal lists if it is even if not one more country for the first half.
middle_of_countries = len(countries) // 2

first_half_countries = countries[:middle_of_countries]
second_half_countries = countries[middle_of_countries:]

print(first_half_countries)
print(second_half_countries)

#37. Unpack the first three countries and the rest as scandic countries.
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

big_names = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_big, second_big, third_big, *scandic = big_names
print(first_big)
print(second_big)
print(third_big)
print(scandic)


