# # For more info on all things Python, use: https://docs.python.org/3/library/
# # Numerical data types
# # - int, long, float, complex
# # These are numerical data types whc we can use numerical operators
# # Complex and long numbers we don't use so much
# # Complex brings and imaginary component to a number
# # Long -
#
# # int - Stands for integers
# # Whole numbers
# my_int = 10
# print(my_int)
# print(type(my_int))
#
# # Opperator - add, subtract, multiply, devide
#
# print(5+6)
# print(8*6)
# print(18/3) # Devisions automatically get converted to float
# print(9-7)
#
# # Modules looks for rhe number of remeinders
# # %
# print(22%5) # --> counts how many remainders are left after the devison. Cant be more than the dividing number
#
# # Comaprrison Operators #--> this outputs a boolean value
#
# # == is the comparison operator
# # < / >  bigger than, smaller than. Adding
# # <= less than or equal to
# # >= bigger than or equal too
# # != is not equal to
# # is and is not
#
# my_variable_1 = 10
# my_variable_2 = 13
#
# print(my_variable_1 == my_variable_2)
# print(my_variable_1 > my_variable_2)
# print(my_variable_1 < my_variable_2)
# print(my_variable_1 >= my_variable_2)
# print(my_variable_1 is 15)
# print(my_variable_2 is not 56)
#
# # Boolean values
# # These are difined as etither true or false
# print(type(True))
# print(type(False))
# print(0 == False)
# print(1 == True)
#
# # None
# print(None)
# print(type(None))

# Logocal AND & OR

a = True
b = False
# Using *and*, both sides have to be true for it to result in true

print(a and True)
print(1 == 1 and True)
print(1 == 1 and False)

# Using OR, only one side needs to be true
# This will print true
print(True or False)
print(True or 1 == 2)

# This will print false
print(False or 1 == 2)
