


# syntax

# for <placeholder> in <iterable>:
    # block of code
    # Indented gets run every iteration

# Dont forget the colon

# cars = ['Skoda Felicia FUN', 'Fiat Panda 4x4', 'Mustang Ford']
#
# for car in cars:
#     print('Hey :D')
#     print(car)

embbeded_list = [['Filipe', 'Francis'], ['Mustafa', 'David', 'Gillian']]

# for data in embbeded_list:
#     print(data)
#     breakpoint()
#     for name in data:
#         print(name)

student_1 = {
    'name': 'Arya Stark',
    'Stream': 'Many Faces',
    'Grade': '10',
    'complete modules': ['sword', 'augmented sense', 'no face', 'no name']
}

# for key in student_1:
#     print(key)
#     print(student_1[key])

# 1 - Name: Arya Stark
# 2 - Stream: Many Face


count_1 = 1
# for key in student_1:
#     print(f' {count_1} - {key}: {student_1[key]}'),
#     count_1 += 1
#
# for key,values in student_1.items():
#     print(count_1, key, values)
#     count_1 += 1

students = {
    'student1': student_1,
    'Student2': {
        'name': 'Stirling Archer',
        'Stream': 'Chaos',
        'Grade': '10',
        'complete modules': ['danger', 'strong liver', 'mummy issues', 'Espionage']
    }
}


# for student_key in students:
#     print(student_key)
#     count_1 = 1
#     print('/////////////////////////////////////')
#     for values in students[student_key]:
#         print(count_1, '-' , key, ':', students[student_key][value] )
#         count_1 += 1

for key1 in students:
    print(key1)
    count_1 = 1
    print('/////////////////////////////////////')
    for key2 in students[key1]:
         print(count_1, '-' , key2, ':', students[key1][key2])
         count_1 += 1
