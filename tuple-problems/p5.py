# find tuple length without using len()
numbers = (1, 2, 3, 4, 5)

# print(len(numbers))
length = 0
for n in numbers:
    length += 1

print(length)