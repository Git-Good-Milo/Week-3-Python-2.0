
# Create a dictionary with 3 stories inside! like a book :)
# each story should be it's own dictionary with:
    # beggining, middle, end
    # hero
# Iterate over the the book, and print out each story! PRINT ALL of them :)
# Formatted of course
# hints:
 # you already built a dictionary with a story
 # You already have something to prompt user for input & build dictionaries
 # Now what we want is to create a book that hold 3 stories

# extra:
 # stick it in a while loop so we continue to listen to stories :)
 # It would be nice to be able to read only one story

story1 = {
    'Start': 'One day, a stupid man was born: Continue',
    'Middle': 'He did not know the bounds of his stupidity: How so?',
    'End': 'As a result, he doomed the human race: Please elabourate'
}

story2 = {
    'Start': 'Far into the future, an unlikely building was made... describe it: ',
    'Middle': 'what was this memorable building made of?: ',
    'End': 'Fantatic story sir! Please write one more!'
}

story3 = {
    'Start': 'This bloke right, he thought he was mad hard',
    'Middle': 'I swear he was bare crazy',
    'End': 'He took himself out in the end! Funny stuff yo!'
}

all_stories = {
    'first_story': story1,
    'second_story': story2,
    'third_story': story3
}
which_story = input('What story whould we listen to first? ')
if which_story in all_stories: #== all_stories['first_story']:
    print(all_stories['first_story'])

#print(f"{story1['start']}. {story1['Middle']}")

