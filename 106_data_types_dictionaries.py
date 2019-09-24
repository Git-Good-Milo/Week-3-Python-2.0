# # All fun and games keeping our crazy ex list... but we also need more info.
# # introducing Dictionaries
#
# # Dictionaries are defind using {}
# # They are organised with keys that pont to a vaule
# # Much like looking up something on a dictinary or information abouot a contact on our phones
# # Thus in our ohone, the contact Filipe Paiva will holdlots of information for this entry. Could be the phone number, work number, address and so on...
# # Syntax:
# ## variable_name = {
# ##    'Example_key': 'value',
# ##    'Example_key2': 'value2'
# ## }
#
# dictionary_crazy_ex = {
#     'Kirsten': 'She was actually nice',
#     'Nicky': 'She was a bit of a drinker!',
# }
# print(dictionary_crazy_ex)
# print(type(dictionary_crazy_ex))
#
# # Accessing values - -use they key
# print(dictionary_crazy_ex['Kirsten'])
# print(dictionary_crazy_ex['Nicky'])
#
# # Adding a new Key, pair value
#
# dictionary_crazy_ex['Kyle'] = 'Drinks too much Monster'
#
# print(dictionary_crazy_ex)
#
# ## Get out all of the keys
# ##print(dictionary_crazy_ex.keys())
#
# dictionary_crazy_ex.pop('Kyle')
# print(dictionary_crazy_ex)


# Better example of a dictionary

crazy_1 = {
    'name': 'Kirsten',
    'phone': '07413065597',
    'address': '3 Earls Road, Alex Park',
    'Know place to avoid': ['Harare', 'Portugal', 'Holland']
}
print(crazy_1)
print(crazy_1['phone'])

# Tuples --> Imutable Lists
# They do not change
# Syntax
# my_tuple = ()

# my_tuple = (2, 'Hello', 22, 'More Value')
# print(my_tuple)
# print(type(my_tuple))
#
# print(my_tuple[0])
#
# my_tuple[0] = 30
# print(my_tuple)