# Assignment for post class
# Ask and store the following in variables:
# Name, last_name, age, age_of_mother, 3_skill
name = input('What is your name warrior? ').strip().capitalize()
last_name = input('And your surname? ').strip().capitalize()
age = int(input('How old are you, mighty stallion? '))

age_of_mother = int(input('And what of the age of your mother? '))
##first_skill = input('What is your best attribute? ').strip().capitalize()
##second_skill = input('What is your second best attribute? ').strip().capitalize()
##third_skill = input('And your most mortal attribute of them all? ').strip().capitalize()
skill_list = [input('What is your best attribute? ').strip().capitalize(),
              input('What is your second best attribute? ').strip().capitalize(),
              input('And your most mortal attribute of them all? ').strip().capitalize()]
# Print out the information in a formatted manor

print(
    f'{name} {last_name}, Is a Godly man!',
    f'Even at the tender age of {age}.',
    f'His exceptional mother is only',
    f'{age_of_mother}, years old'
)

# Calculate age difference between responce and mother

print(f'The age difference is imense, '
    'at',
    (age_of_mother) - (age),
    'years!'
)

# Store skills in a list
##skills_list = [first_skill, second_skill, third_skill]
# Print each skill in a formatted way
print(
    f'{name} '
    f'{last_name} '
    f'has the most {skill_list[0]} of all the men in the Galaxy!',
    f'His {skill_list[1]} is unmatched by any mortal being.',
    f'Even lightning struggles to keep up with his {skill_list[2]}'
)
#  Definition of Fromatted:
## A liitle context text, and approproaite string formatiing like lowercase, uppercase etc