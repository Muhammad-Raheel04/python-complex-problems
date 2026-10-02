# remove all duplicates and print the result.
# Then, print the list sorted in descending order.

nums = [1, 2, 2, 3, 4, 4, 4, 5]
numbers = set()

for n in nums:
    numbers.add(n)

# duplicated removed
print(numbers)

# descending
result = sorted(numbers, reverse=True)

print(result)
