# Count Even and Odd Numbers in tuple
numbers = (1, 3, 4, 5, 6, 7, 8, 9, 10)

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print(even)
print(odd)
