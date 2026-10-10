# Given two lists:
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# Use a set comprehension to find the 
# intersection (common elements) of these two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection={n for n in set(list1) & set(list2)}
print(intersection)