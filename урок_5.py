# словари, множества

# class 'dict'-словари
# {key:value}

students = {
    'name': 'Anna',
    'age': 19,
    'height': 1.6,
    'married': False,
    'hobby': ['chess', 'english', 'books'],
    'education': ('school', 'english C1', 'Python')
}
for i in students:
    print(i, ':' ,students[i])
"""add"""
students['surname'] = 'Walker'
students['hobby'].append('boxing')
students.update('')

'''edit'''
students['height'] = 1.7
students['education'] = list(students['education'])
students['hobby'][0] = 'football'

"""delete"""
del students['married']
students.pop('height')

"""множествo-set"""
# num = [1, 2, 3, 1, 4, 5, 2, 3]
# num1 = {1, 2, 3, 1, 4, 5, 2, 3}
# print(num)
# print(num1)
# print(type(num1))



