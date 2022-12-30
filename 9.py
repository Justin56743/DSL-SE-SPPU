def add_matrices(A, B):
  # Check that the matrices have the same size
  if len(A) != len(B) or len(A[0]) != len(B[0]):
    raise ValueError("Matrices are not of the same size")

  # Add the matrices element-wise
  result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
  return result

def subtract_matrices(A, B):
  # Check that the matrices have the same size
  if len(A) != len(B) or len(A[0]) != len(B[0]):
    raise ValueError("Matrices are not of the same size")

  # Subtract the matrices element-wise
  result = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
  return result

def multiply_matrices(A, B):
  # Check that the matrices are compatible for multiplication
  if len(A[0]) != len(B):
    raise ValueError("Matrices are not compatible for multiplication")

  # Multiply the matrices
  result = [[sum([A[i][k] * B[k][j] for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]
  return result

def transpose_matrix(A):
  # Transpose the matrix
  result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
  return result

# Test the functions with sample matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(add_matrices(A, B))  # Output: [[6, 8], [10, 12]]
print(subtract_matrices(A, B))  # Output: [[-4, -4], [-4, -4]]
print(multiply_matrices(A, B))  # Output: [[19, 22], [43, 50]]
print(transpose_matrix(A))  # Output: [[1, 3], [2, 4]]
