# Count an Element
numbers = (1, 2, 2, 3, 3, 3, 4, 4, 5, 6)
count = 0
for n in numbers:
    if n == 2:
        count += 1

print("Item occurrence ", count)

# alternative solution
print("Item occurrence ", numbers.count(2))
