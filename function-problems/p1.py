# Write a function that accepts any number
# of numbers and returns their sum (*args).


def add(*args):
    return sum(args)

print(add(1,2,3,4))