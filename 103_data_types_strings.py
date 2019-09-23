# String
# A list of characters that are put together.
# Defined by eitehr ' ' or " "

my_string = 'Amazing grilled fish'
print(type(my_string))
print(my_string)

# Joining of strings (Concatenation)
first_name = 'Boris'
last_name = 'Becker'
full_name = first_name + ' ' + last_name
print(full_name)
print('string', 14)
print(full_name[0])

# Interpolation
name = 'Rachel'
welcome_message = 'Hey there, How youuu doin?'
print(f'Hey there, {name} How youuu doin?')
# before the string, place an f
# Then you can use  the {} tto interpolate python variables inside)


my_string = '   This fish really is something else! '

# .count() counts the number of time a character appears
print(my_string.count('i'))
print(my_string.count(' '))

# .strip() removes blank spaces in a string
print(my_string.strip())

# len() provides the length of a string. Not a method! General Method built in
print(len(my_string))

#.lower()
print(my_string.lower())

#.upper()
print(my_string.upper())

#.capitilise()
print(my_string.strip().capitalize().count('j'))

#.replace(arg_int, arg_two)
print(my_string.replace('is', 'IS'))
