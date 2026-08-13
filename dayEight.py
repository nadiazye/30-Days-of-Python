# Day 8 out of 30 Days of Python Challenge
#=======================================================================================================================
#Dictionaries
#A dictionary is a collection of unordered, modifiable (mutable) paired (key: value) data type

#Creating a Dictionary
#To create a dictionary we use curly brackets, {} or the dict() built-in function
"""syntax:
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}"""

person = {
    'first_name': 'Nadia',
    'last_name': 'Rodriguez',
    'age': 22,
    'country': 'USA',
    'is_married':False,
    'skills':['Java','Python','HTML','CSS'],
    'address' : {
        'street': '123 Main Street',
        'zipcode': '12345'
    }
}
#This dictionary above shows that a value could be any data types: string, boolean, list, tuple, set, or a dictionary

#Dictionary Length
#It checks the number of 'key:value' pairs in the dictionary
"""syntax:
dct = {'key1:'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)"""

person = {
    'first_name': 'Nadia',
    'last_name': 'Rodriguez',
    'age': 22,
    'country': 'USA',
    'is_married':False,
    'skills':['Java','Python','HTML','CSS'],
    'address' : {
        'street': '123 Main Street',
        'zipcode': '12345'
    }
}
print(len(person))

#Accessing Dictionary Items
#We can access Dictionary items by referring to its key name
"""syntax:
dct = {'key1:'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) (would say value1)
print(dct['key4']) (would say value4)"""

print(person['first_name'])
print(person['last_name'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['street'])
# print(person['city']) #Should return an error (did return error)

#Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if
#a key exist, or we can use the get method. The get method returns None, which is a NoneType object data type,
# if the key does not exist.

print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))

#Adding Items to a Dictionary
#We can add new key and value pairs to a dictionary
"""syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'"""

person['job_title'] = 'Instructor'
person['skills'].append('C#')
print(person)

#Modifying Items in a Dictionary
#We can modify items in a dictionary
"""# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'"""

person['first_name'] = 'Aidan'
person['age'] = 222

#Checking Keys in a Dictionary
#We use the in operator to check if  akey exist in a dictionary
""""syntax:
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False """

#Removing Key and Value Pairs from a Dictionary
#pop(key): removes the item with the specified key name
#popitem(): removes the last item
#del: removes an item with specified key name

"""syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item """

person.pop('first_name')
person.popitem()
del person['is_married']

#Changing Dictionary to a List of Items
#The items() method changes dictionary to a list of tuples
"""syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])"""

#Clearing a Dictionary
#If we don't want the items in a dictionary we can clear them using clear() method
"""syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None"""

#Deleting a Dictionary
#If we do not use the dictionary we can delete it completely
"""syntax:
dct = {'key1:'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct}"""

#Copy a Dictionary
#We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary
"""syntax:
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}"""

#Getting Dictionary Keys as a List
#The keys() method gives us all the keys of a dictionary as a list
"""syntax:
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])"""

#Getting Dictionary Values as a List:
#The values method gives us all the values of a dictionary as a list
"""syntax:
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])"""

#=======================================================================================================================
#Exercises
#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Sparky', 'color':'brown', 'breed':'Doberman','legs':4, 'age': 3}

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country,
# city and address as keys for the dictionary
student = {
    'first_name':'Sparky',
    'last_name':'Rodriguez',
    'gender':'Male',
    'age':3,
    'marital_status':'Married',
    'skills':['Bark','Woof','Run','Jump'],
    'country':'Barkania',
    'address':{
        'street': '123 Woof Street',
        'zipcode': '12345'
}
}

#4. Get the length of the student dictionary
print(len(student))

#5. Get the value of skills and check the data type, it should be a list
skill_values = student['skills']
print(skill_values)
print(type(skill_values))

#6. Modify the skills values by adding one or two skills
student['skills'].append('Howl')

#7. Get the dictionary keys as a list
keys = student.keys()
print(keys)

#8. Get the dictionary values as a list
values = student.values()
print(values)

#9. Change the dictionary to a list of tuples using items() method
print(student.items())

#10. Delete one of the items in the dictionary
dog.popitem()

#11. Delete one of the dictionaries
del dog