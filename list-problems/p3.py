# Return a new list without duplicates.

numbers = [1, 2, 3, 2, 4, 1, 5, 3]


def remove_duplicates(numbers):
    normalized_numbers = []
    for n in numbers:
        if n not in normalized_numbers:
            normalized_numbers.append(n)

    return normalized_numbers

print(remove_duplicates(numbers))
