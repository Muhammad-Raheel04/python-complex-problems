# Given a list of words
# words = ["apple", "bat", "cat", "elephant"],
# create a dictionary where the word is the
# key and its length is the value, but only
# for words with length greater than 3.

words = ["apple", "bat", "cat", "elephant"]

words = {k: len(k) for k in words if len(k) > 3}

print(words)
