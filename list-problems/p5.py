# Given a list of integers and a
# target value, return the indices
# of two numbers that add up to the target.

numbers = [2, 7, 11, 15]
target = 9

for n in range(len(numbers)):
    for j in range(n + 1, len(numbers)):
        if numbers[n] + numbers[j] == target:
            print([n, j])
