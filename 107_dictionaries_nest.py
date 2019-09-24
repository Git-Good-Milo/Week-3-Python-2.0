# nested_list = ['bread', 'sugar', [1, 2, 3, 4, 'spice']]
#
# bread = nested_list[0]
# nested = nested_list[2]
#
# print(type(bread))
# print(type(nested[4]))
#
# print(nested_list[2][4])
#
# print(nested_list[2][5]['name'])

student_1 = {
    'name': 'Arya Stark',
    'Stream': 'Many Faces',
    'Grade': '10',
    'complete modules': ['sword', 'augmented sense', 'no face', 'no name']
}
students = {
    'student1': student_1,
    'Student2': {
        'name': 'Stirling Archer',
        'Stream': 'Chaos',
        'Grade': '10',
        'complete modules': ['danger', 'strong liver', 'mummy issues', 'Espionage']
    }
}

breakpoint()

print(students['student1']['name'])