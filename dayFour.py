#Day 4 out of the 30 Days of Python Challenge
#=======================================================================================================================
'''
Strings
Text is a string data type. Any data type written as text is a string. Any data under single, double, or triple
quotes are strings. There are different string methods and built-in functions to deal with string data types.
To check the length of a string use the len() method
'''
from dayTwo import first_name

letter = 'P' #A string could be a single character or multiple texts
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = 'I hope you are enjoying this challenge'
print(sentence)

#A multiline string is created by triple single quotations (''') or triple double quotes (""")
multiline_string = '''Hi my name is Nadia and I am 22.
Comp Sci student at the UM.'''
print(multiline_string)

#We are able to connect strings concatenation
first_name = 'Nadia'
last_name = 'Rodriguez'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

'''Escape Sequences in Strings
In python and other programming languages (one)\ followed by a character is an escape sequence. Most common are
\n: new line
\t: Tab
\\: backslash
\': Single quote(')
\": Double quote (")
Examples below:'''

print('I hope everyone is having a good day. /n Are you ?')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t33')
print('Day 4\t1\t45')
print('This is  backslash symbol (\\)')

''' String formatting
Old Style String Formatting (% Operator)
In python there are many ways of formatting strings. The "%" operator is used to format a set of
variables enclosed in a "tuple" ( a fixed size list), together with a format string, which contains normal text
together with "argument specifiers", special symbols like "%s","%d","%f", "%number of digitsf"
%s - string (or any object with a string representation, like #
%d - Integers
%f - floating point numbers
"%.number of digitsf" - floating point numbers with fixed position
Examples below:'''

#Strings
first_name = 'Nadia'
last_name = 'Rodriguez'
language = 'Python'
formatted_string = "I am %s %s. I teach %s" %(first_name, last_name, language)
print(formatted_string)

#Strings and numbers
radius = 10
pi = 3.14
area = pi * radius**2
formatted_string = "The area of circle with a radius %d is %.2f.",(radius,area)

python_libraries = ['Django', 'Flask','NumPy','Matplotlib', 'Pandas']
formatted_string = 'The following are python libraries:%s' % python_libraries
print(formatted_string)

#New Style String Formatting
first_name = 'Nadia'
last_name = 'Rodriguez'
language = 'Python'
formatted_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formatted_string)
a = 4
b = 3

print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))

#Strings and numbers
radius = 10
pi = 3.14
area = pi * radius**2
formatted_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formatted_string)

#String Interpolation/ f - Strings
#Another new string formatting is string interpolation, f-string. Strings start with f
# and we can inject the data in their corresponding positions
a = 4
b = 3
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')

#Python Strings as Sequences of Characters
'''python strings are sequences of characters, and share their basic methods of access with other python ordered 
sequences of objects - lists and tuples. The simplest way of extracting single characters from strings (and individual members
from any sequence) is to unpack them into corresponding variables '''

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Accessing Characters in Strings by Index
'''In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter
of a string is the length of a string minus one'''

language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
#We can also start from the right end by using negative indexing
language = 'Python'
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

#Slicing Python String : In oython we can slice strings into substrings
language = 'Python'
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)

#Another example
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

#Reversing a String : We can easily reverse strings in python
greeting = 'Hello, World!'
print(greeting[::-1])

#Skipping characters while slicing : It is possible to skip characters while slicing by passing step argument to slicing method
langauge = 'Python'
pto = language[0:6:2]
print(pto)

#String Methods:
# capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize())

#count(): returns occurrences of substring in string, count(substring, start=, end =) The start is a starting index for counting and end is the last index to count
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y',7,14))
print(challenge.count('th)'))

#endswith(): checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

#expand tabs(): Replaces tab character with spaces, default tab size is 8 -- it takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

#rfind(): returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))

#format(): formats string into a nicer output
first_name = 'Nadia'
last_name = 'Rodriguez'
age = 22
job = 'student'
country = 'USA'
sentence = 'I am {} {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius**2
result = 'The area of a circle with a radius {} is {}.'.format(str(radius), str(area))
print(result)

'''index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index
(default 0 and string length - 1) if the substring is not found it raises a valueError'''
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
#print(challenge.index(sub_string,9))

#rindex(): returns the highest index of a substring, additional arguments indicate starting and ending index
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))
#print(challenge.rindex(sub_string,9))
print(challenge.rindex('on',8))

#isalnum(): checks alphanumeric character
challenge_1 = 'thirtydaysofpython'
print(challenge_1.isalnum())

challenge_2 = '30daysofpython'
print(challenge_2.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum())  #False because space does not count as an alphanumeric character

#isalpha(): checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) #false because there are spaces

print(challenge_1.isalpha())

num = '123'
print(num.isalpha())

#isdecimal(): Checks if all characters in a string are decimal (0-9)
print(challenge.isdecimal())

challenge_3 = '123'
print(challenge_3.isdecimal())

challenge_4 = '\u00B2'
print(challenge_4.isdigit())

challenge_5 = '12 3'
print(challenge_5.isdecimal()) #space is still not allowed

#isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge_6 = 'Thirty'
print(challenge_6.isdigit())

challenge_7 = '30'
print(challenge_7.isdigit())

print(challenge_4.isdigit())

#isnumeric(): Checks if all characters in a string are numbers or number related (similar to isdigit(), more accepting)
num = '10'
print(num.isnumeric())

num_1 = '\u00BD' # = 1/2
print(num_1.isnumeric())

num_2 = '10.5'
print(num_2.isnumeric())

#isidentifier(): Checks for valid identifier - it checks if a string is a valid variable name
challenge_8= '30DaysOfPython'
print(challenge_8.isidentifier()) # False, because it starts with a number

challenge_9 = 'thirty_days_of_python'
print(challenge.isidentifier())

#islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

#isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

#join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)

#strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

#replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

#split(): Splits the strong, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

#title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

#swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to upper characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON

challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
#startswith(): checks if string starts with the specified string
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

#=======================================================================================================================
print('================================================================================================================')
#Day 4 Exercises
#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
number = 'Thirty'
days = 'Days'
article = 'Of'
language = 'Python'
space = ' '

full_sentence = number + space + days + space + article + space + language
print(full_sentence)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
action = 'Coding'
article = 'For'
who = 'All'
full_statement = action + space + article + space + who
print(full_statement)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())

print(company.title())

print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
first_gone = company[0:6] #need to rewrite
print(first_gone)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding')) #need to rewrite

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))

#Change "Python for Everyone" to "Python for All" using the replace method or other methods.
language_for = 'Python for Everyone'

print(language_for.replace('Everyone','All'))

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split( ))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(tech_companies.split(','))

#What is the character at index 0 in the string Coding For All.
print(company[0])

#What is the last index of the string Coding For All.
print(company[-1])

#What character is at index 10 in "Coding For All" string.
print(company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = language_for[0:7:11]
print(acronym)

#Create an acronym or an abbreviation for the name 'Coding For All'.
acronym_second = company[0:7:11]
print(acronym_second)

#Use index to determine the position of the first occurrence of C in Coding For All.

#Use index to determine the position of the first occurrence of F in Coding For All.

#Use rfind to determine the position of the last occurrence of l in Coding For All People.

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#Does 'Coding For All' start with a substring Coding?

#Does 'Coding For All' end with a substring coding?

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
'''Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python '''

#The following list contains the names of some python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

'''Use the new line escape sequence to separate the following sentences.

I am enjoying this challenge.
I just wonder what is next. '''

'''Use a tab escape sequence to write the following lines.

Name      Age     Country   City
Asabeneh  250     Finland   Helsinki'''

'''Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.

'''

'''Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144 '''