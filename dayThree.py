#Day Three out of 30 Days of Python Challenge

'''Assignment Operators: are used to assign value to variables, Examples below:
=, x = 5, x=5
+=, x + 3, x=x+3
-=, x -= 3, x = x-3
*=, x *= 3, x = x*3
/=, x /= 3, x = x/3
%=, x %= 3, x = x%3
//=, x //= 3, x = x//3
**=, x **= 3, x = x**3
&=, x &= 3, x = x&3
|=, x |= 3, x = x|3
^=, x ^= 3, x = x^3
>>=, x >>= 3, x = x>>3
<<=, x <<= 3, x = x<3
'''
#=======================================================================================================================
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2
#-----------------------------------------------------------------------------------------------------------------------
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
#-----------------------------------------------------------------------------------------------------------------------
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
#-----------------------------------------------------------------------------------------------------------------------
# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type
#-----------------------------------------------------------------------------------------------------------------------
# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4
#-----------------------------------------------------------------------------------------------------------------------
# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one
#-----------------------------------------------------------------------------------------------------------------------
# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

#Now using these functions above to solve problems ---------------------------------------------------------------------
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density
#-----------------------------------------------------------------------------------------------------------------------
#Comparison Operators, we use these when comparing values -- to check if a value is greater or lesser or equal to the other
'''
==, Equal, x == y
!=, Not equal, x != y
>, Greater than, x > y
<, Less than, x < y
>=, Greater than or equal to, x >= y
<=, Less than or equal to, x <= y
Example below'''
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
# In addition to the abpve comparison operator Python also uses:
'''
is: Returns true if both variables are the same object(x is y)
is not: Returns true if both variables are not the same object (x is not y)
in: Returns true if the queried list contains a certain item (x in y)
not in: Returns True if the queried list doesn't have a certain item (x not in y)
Example below'''

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

#Logical Operators, logical operators are used to combine conditional statements
'''
and | Returns true if both statements are true
or | Returns true if one of the statements are true
not | Reverse the result, returns False if the result is true
Examples below'''

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
#=======================================================================================================================
#Day 3 Exercises:
age = 22
height = 5.3
complex_num = 1 + 1j
base_of_triangle = input("Please enter the base of a triangle: ")
height_of_triangle = input("Please enter the height of the triangle: ")
area_of_triangle = float(base_of_triangle) * float(height_of_triangle)
print("The area of the triangle is " ,(float(area_of_triangle)))

side_a_of_triangle = input("Please enter the side A of a triangle: ")
side_b_of_triangle = input("Please enter the side B of a triangle: ")
side_c_of_triangle = input("Please enter the side C of a triangle: ")
triangle_perimeter = (int(side_a_of_triangle)) + (int(side_b_of_triangle)) + (int(side_c_of_triangle))
print("The perimeter of the triangle is ", (int(triangle_perimeter)))

length_of_rectangle = input("Please enter the length of a rectangle: ")
width_of_rectangle = input("Please enter the width of a rectangle: ")
rectangle_area = float(length_of_rectangle) * float(width_of_rectangle)
print("The area of the rectangle is ", (float(rectangle_area)))
rectangle_perimeter = (float(length_of_rectangle) + float(width_of_rectangle)) * 2
print("The perimeter of the rectangle is ", (float(rectangle_perimeter)))

radius_of_circle = input("Please enter the radius of a circle: ")
area_of_circle = 3.14 * float(radius_of_circle) ** 2
print("The area of the circle is ", (float(area_of_circle)))
perimeter_of_circle = 3.14 * float(radius_of_circle) ** 2
print("The perimeter of the circle is ", (float(perimeter_of_circle)))


