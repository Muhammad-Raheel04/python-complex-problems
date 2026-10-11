# Given a dictionary
# prices = {'apple': 1.0, 'banana': 0.5, 'orange': 0.8},
# create a new dictionary where the keys
# and values are swapped.
# Expected Output:
# {1.0: 'apple', 0.5: 'banana', 0.8: 'orange'}

prices = {"apple": 1.0, "banana": 0.5, "orange": 0.8}

prices={y:k for k,y in prices.items()}
print(prices)
