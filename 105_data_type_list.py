# List
# List keep objects in order of index.
# Its defined by square brackets []
# Lists are organised with Index
# example of a list
# list_name = [0, 1, 2, 3, 4, 5]

crazy_ex_partners = ['Kirsten', 'Nicky', 'Archer', 'Cyril', 'Malorie', 'Pam', 'Cheryl']

print(crazy_ex_partners)
print(type(crazy_ex_partners))


# remove someone from the list (Destroy one)
crazy_ex_partners.remove('Cyril')

# Remove using the index
crazy_ex_partners.pop()
print(crazy_ex_partners)

# Add someone to the list (Create One). Usually you append()
# .insert is used to insert into the list at a specific index point
print(crazy_ex_partners)
crazy_ex_partners.append('Kreiger')
print(crazy_ex_partners)


# Selecting a particular record (read one)
print(crazy_ex_partners[0])

# Edit an entry or re-assign at an Index
crazy_ex_partners[6] = 'LAANNAA!'
print(crazy_ex_partners[6])

# Lists can have many data types
hybrid_list = ['This is a string', 12, 66, 'hello', [1,2,3], [4,5,6]]

# WHat happens when you have 350000000 records?
# Answer is loops and other methods!