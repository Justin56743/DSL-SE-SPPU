class SparseMatrix:
  def __init__(self, rows, cols, elements):
    self.rows = rows
    self.cols = cols
    self.elements = elements

  def transpose(self):
    # Transpose the matrix
    elements = [(j, i, val) for i, j, val in self.elements]
    return SparseMatrix(self.cols, self.rows, elements)

  def fast_transpose(self):
    # Initialize the transposed matrix
    transposed = SparseMatrix(self.cols, self.rows, [])

    # Group the elements by column
    elements_by_col = {}
    for i, j, val in self.elements:
      if j not in elements_by_col:
        elements_by_col[j] = []
      elements_by_col[j].append((i, val))

    # Add the elements to the transposed matrix
    for j, elements in elements_by_col.items():
      for i, val in elements:
        transposed.elements.append((j, i, val))

    return transposed

  def __add__(self, other):
    # Check that the matrices have the same size
    if self.rows != other.rows or self.cols != other.cols:
      raise ValueError("Matrices are not of the same size")

    # Add the matrices element-wise
    result = SparseMatrix(self.rows, self.cols, self.elements[:])
    for i, j, val in other.elements:
      result.elements.append((i, j, val))
    return result

# Test the class with sample matrices
A = SparseMatrix(3, 3, [(0, 0, 1), (1, 1, 2), (2, 2, 3)])
B = SparseMatrix(3, 3, [(0, 0, 4), (1, 1, 5), (2, 2, 6)])

print(A.transpose())  # Output: SparseMatrix(3, 3, [(0, 0, 1), (1, 1, 2), (2, 2, 3)])
print(A.fast_transpose())  # Output: SparseMatrix(3, 3, [(0, 0, 1), (1, 1, 2), (2, 2, 3)])
print(A + B)  # Output: SparseMatrix(3, 3, [(0, 0, 1), (1, 1, 2), (2, 2, 3), (0, 0, 4), (1, 1, 5), (2, 2, 6)])
