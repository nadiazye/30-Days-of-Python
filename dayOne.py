# Day 1 out of 30 Days of Python Challenge

print("hello world")

print(2+3) #addition
print(3-1) #subtraction
print(2*3) #multiplication
print(3/2) #division
print (3**2) #exponential
print(3%2) #modulus
print(3//2) #floor division operator

# explanation for exponential, modulus, and floor division operator
    # exponential - would be the number a to x power
    # modulus - would be the remainder of dividing two numbers, commonly used to check even or odd numbers and
        # to create repeating cycles in loops
    # floor division operator - divides two numbers and rounds down to the nearest whole number (ex. 10//3 will return 3)

# checking data types
print(type(10)) #Integer
print(type(3.14)) #Float
print(type(1+3j)) #Complex number
print(type('Asabeneh')) #string
print(type([1,2,3])) #List
print(type({'name':'Asabeneh'})) #Dictionary
print(type({9.8,3.14,2.7})) #Set
print(type((9.8,3.14,2.7))) #Tuple

 # explanation for complex number, dictionary, set, and tuple
 # complex number - a number that has both a real part and an imaginary part
 # dictionary - mutable collection of key-value pairs, where each key is unique and is used to access its corresponding value
 # defined using curly braces
 # set - an unordered collection of unique elements, does not allow duplicate items and does not maintain any specific order
 # tuple - a collection of ordered and immutable elements, meaning once created, you cannot change or modify the elements

#=======================================================================================================================
 #Exercises for Day 1

 #Exercise Level 1

 #check the python version you are using
print("I am using the Python version 3.13")

 #Open the python interactive shell and do the following operations, using the numbers 3 and 4

print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

 #Write strings on the python interactive shell
print("My name is Nadia Rodriguez")
print("My family is made of Rodriguez's and Perez's")
print("I am from the United States of America, but my parents are from Cuba and Puerto Rico")
print("I am enjoying 30 days of python :D")

#check the data types for the following data
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python','Finland']))
print(type("Nadia"))
print(type("Rodriguez"))
print(type("USA"))
#-----------------------------------------------------------------------------------------------------------------------
#Exercise 3, write an example for different Python data types
print(1) #int
print(2.1) #float
print(3-3j) #complex
print("Hahahahaha") #string
print(10 > 9) #boolean
print(10 < 9) #boolean
print(10 == 9) #boolean
print(['Me','You','Us']) #list
print(1.2,2.4,3.5) #tuple
print({1.2,2.4,3.5})#set
print({'name':'Nadia the Best'})#dictionary

#-----------------------------------------------------------------------------------------------------------------------
#Find a Euclidean distance between (2,3) and (10,8) p1 = 2, p2 = 3, q1 = 10, q2 = 8
#Euclidean distance = d(p,q)^2 = (q1-p1)^2 + (q2-p2)^
print((10-2)**2 + (8-3)**2)