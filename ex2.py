my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}


age = my_dict['age']

my_dict['salary'] = 50000


for i, j in my_dict.items():
    print(f'{i}: {j}')

my_dict_2 = {}
for key, val in my_dict.items():
    my_dict_2[val] = key
print(my_dict_2)


