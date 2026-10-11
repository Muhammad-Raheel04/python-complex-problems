# Write a function that accepts a dictionary
# of options and prints them (**kwargs).


def printDict(**kargs):
    print(kargs)


options = {"theme": "dark", "font_size": 16, "language": "Python"}

print(printDict(**options))
