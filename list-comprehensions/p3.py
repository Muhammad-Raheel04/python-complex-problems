# Given a 2D matrix 
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
# use a list comprehension to flatten it into
# a single 1D list.
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix[:]=[item for row in matrix for item in row]
print(matrix)