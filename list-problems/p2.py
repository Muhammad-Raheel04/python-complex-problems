# Write a program to count how many times 2 appears.

numbers = [1, 2, 3, 2, 4, 2, 5]

count = 0
for n in numbers:
    if n == 2:
        count += 1

print(count)        
