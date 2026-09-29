# Given a list of integers, return a
# dictionary containing the frequency of each element.
# The frequency of an element is the number of
# times it appears in the list.

numbers = [1, 2, 3, 4, 5, 6, 6] # list unlike tuple they are mutatble


def count_frequency(numbers):
    frequency = {} # dictonary

    for n in numbers:
        frequency[n] = frequency.get(n, 0) + 1

    return frequency


print(count_frequency(numbers))
