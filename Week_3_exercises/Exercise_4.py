# Dictionary basics :D
#1 - Define a dictionary call story1, it should have the followign keys:
        # Start, Middle and End

story1 = {
    'Start': 'One day, a stupid man was born',
    'Middle': 'He did not know the bounds of his stupidity',
    'End': 'As a result, he doomed the human race'
}
#2 - Print the entire dictionary

print(story1)

#3 - Print the type of your dictionary

print(type(story1))

#4 - Print only the keys

print(story1.keys())

#4 - print only the values

print(story1.values())

#5 - print the first each individual value using the keys
print(story1['Start'])
print(story1['Middle'])
print(story1['End'])

#6 - Now let's add a new key: value pair.
    # 'hero': 'Your superhero'

story1['Hero'] = 'Spiderman'
print(story1)

