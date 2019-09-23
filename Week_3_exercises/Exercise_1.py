# Define the following variables
# Name, last name, age, eye colour, hair coulour
name = 'Milo'
last_name = 'Eastwood'
age = 26
eye_colour = 'green'
hari_colour = 'black'


# Prompt users for input and reassign these
name = input('What is your name ')
last_name = input('And your last name? ')
age = input('How old are you? ')
eye_colour = input('What colour are your eyes? ')
hair_colour = input('What colour is your hair? ')


##Print them back to the user as conversation
##Example: 'Hello jack! Welcome, your age is 26, your eyes are green and your...'
print(f'Hello {name} {last_name}! Welcome, your age is {age}! You lying bastard!?! your eyes are blue not {eye_colour}.')
print(f'And i bet you dyed your hair {hair_colour}!')

##Section 2 - Calculate in what year was the person born? and respond back
##Print something like : 'You said we're 28 hence you were born in 1991!'
##Extra - Cast your input
# years_age = 28
# year_born = 2019 - years_age
# print(f'You said you were {years_age}! Therefore you were born in {year_born}')