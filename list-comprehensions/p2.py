# Given a list of strings
# words = ["hello", "world", "python", "code"],
# create a new list where every string is
# capitalized and has its length appended to it.
# Expected Output:
# ['Hello: 5', 'World: 5', 'Python: 6', 'Code: 4']
words = ["hello", "world", "python", "code"]

words[:] = [n.capitalize() + ": " + str(len(n)) for n in words]

print(words)

