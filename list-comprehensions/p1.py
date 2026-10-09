# Given a list of integers
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# create a new list that contains the squares
# of only the even numbers.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenSquareList=[n**2 for n in nums if n%2==0]
print(evenSquareList)
