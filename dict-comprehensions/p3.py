# Given two lists:
# keys = ['name', 'age', 'city', 'country']
# values = ['Alice', 25, 'New York', 'USA']
# Use a dict comprehension with zip() to
# create a dictionary. Then, create a second
# dict comprehension that filters out any
# key-value pair where the value is an integer.

keys = ["name", "age", "city", "country"]
values = ["Alice", 25, "New York", "USA"]

result = {k: v for k, v in zip(keys, values)}

filteredDict={k:v for k,v in result.items() if isinstance(v,int)}

print(filteredDict)
