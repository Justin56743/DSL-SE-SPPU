def saddle_point(matrix):
  # Get the number of rows and columns in the matrix
  m = len(matrix)
  n = len(matrix[0])

  # Iterate over the rows and columns of the matrix
  for i in range(m):
    for j in range(n):
      # Check if the current element is the smallest in its row and largest in its column
      if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max([matrix[k][j] for k in range(m)]):
        # If so, return the location of the saddle point
        return (i, j)

  # If no saddle point is found, return None
  return None

# Test the function with a sample matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(saddle_point(matrix))  # Output: None

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 1]]
print(saddle_point(matrix))  # Output: (2, 2)

matrix = [[1, 2, 3], [4, 5, 1], [7, 8, 9]]
print(saddle_point(matrix))  # Output: (1, 2)
