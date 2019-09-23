# All fun and games keeping our crazy ex list... but we also need more info.
# introducing Dictionaries

# Dictionaries are defind using {}
# They are organised with keys that pont to a vaule
# Much like looking up something on a dictinary or information abouot a contact on our phones
# Thus in our ohone, the contact Filipe Paiva will holdlots of information for this entry. Could be the phone number, work number, address and so on...
# Syntax:
## variable_name = {
##    'Example_key': 'value',
##    'Example_key2': 'value2'
## }

dictionary_crazy_ex = {
    'Kirsten': 'She was actually nice',
    'Nicky': 'She was a bit of a drinker!',
}
print(dictionary_crazy_ex)
print(type(dictionary_crazy_ex))

# Accessing values - -use they key
print(dictionary_crazy_ex['Kirsten'])
print(dictionary_crazy_ex['Nicky'])

# Adding a new Key, pair value

dictionary_crazy_ex['Kyle'] = 'Drinks too much Monster'

print(dictionary_crazy_ex)

## Get out all of the keys
print(dictionary_crazy_ex.keys())