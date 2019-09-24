# Assignment 2 for post class

# Define an empty dictionary: name_dict = {}

# Prompt user for input for story.
hero = input('Who are you legend? ')
beginning = input('Give a description of your legend ')
middle =  input('Give us a short story for the middle')#His ultimate ability to make custard was known throughout time and space.
end = input ('Give us an epic ending') #'As a result, the Gods errected a galaxy sized statue, made of stars in honor of his tasty desert.'
# It should have:
#   Hero, beginning, middle, end.
name_dict = {
    'Hero': hero,
    'beginning': beginning,
    'middle': middle,
    'end': end,

}
#   2 other things you define to be part of the story
name_dict['credits'] = 'Credits:','Stone Cold', 'Shiva', 'God', 'Timmy'
name_dict['disclaimer'] = 'disclaimer': 'Any likeness to any people or dietys is strictly coincidental and a product of chance.'
#   Add each response to the dictionary under the appropriate key

# Print out the dictionary information in an ordered was so we can read the story.
print('The birth of the universe gave life to a legend, known only as:', (name_dict['Hero']))
print(name_dict['Hero'])
print(name_dict['middle'])
print(name_dict['end'])
print(name_dict['credits'])
print(name_dict['disclaimer'])