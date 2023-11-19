dictionary = {
 "name": "John",
 "age": 30,
 "city": "New York" 
}
age = dictionary["age"]

dictionary["salary"] = 50000
print(dictionary)

for i in dictionary.keys():
    print(f"key: {i}")

for i in dictionary.values():
    print(f"value: {i}")

for i,j in dictionary.items():
    print(f"key:{i}, value: {j}")

my_dict_2 = {
    value: key for key, value in dictionary.items()}
print(my_dict_2)

my_dict_3 = {}
