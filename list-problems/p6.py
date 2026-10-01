# Move All Zeros to End
numbers = [0, 1, 0, 3, 12]


# my solution
def move_zeros(numbers):
    newNumbers = []
    count = 0
    for n in numbers:
        if n == 0:
            count += 1
        elif n != 0:
            newNumbers.append(n)
    for n in range(count):
        newNumbers.append(0)

    return newNumbers


print(move_zeros(numbers))


# alternative
def move_zeros_to_end(numbers):
    insert_position = 0

    for n in numbers:
        if n != 0:
            numbers[insert_position] = n
            insert_position += 1

    while insert_position < len(numbers):
        numbers[insert_position] = 0
        insert_position += 1

    return numbers


print(move_zeros(numbers))
