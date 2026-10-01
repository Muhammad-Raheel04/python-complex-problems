# Write a program to find the largest number without using max().

numbers = [12, 45, 7, 89, 23, 56]

maxNumber = numbers[0]
for n in numbers:
    if n > maxNumber:
        maxNumber = n

print(maxNumber)
