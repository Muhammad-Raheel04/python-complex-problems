# Find the Index
animals = ("cat", "mouse", "dog")

# print index of cat
print("Cat index ",animals.index("cat"))

# print indexes of all items in the tuple
for index, animal in enumerate(animals):
    print(index, animal)
