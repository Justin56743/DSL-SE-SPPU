def magic_square(n):
  # Initialize the magic square with zeros
  square = [[0 for i in range(n)] for j in range(n)]

  # Initialize the position of the first element
  row = 0
  col = n // 2

  # Generate the magic square
  for i in range(1, n**2 + 1):
    square[row][col] = i
    row -= 1
    col += 1

    # Check if the next position is out of bounds and adjust accordingly
    if row == -1:
      row = n - 1
    if col == n:
      col = 0

    # Check if the next position is already filled and adjust accordingly
    if square[row][col] != 0:
      row += 2
      col -= 1
      if row == n:
        row = 0
      if col == -1:
        col = n - 1

  # Calculate the sum of the elements in the first row
  magic_sum = sum(square[0])

  # Print the magic square
  for row in square:
    print(row)

  # Print the magic sum
  print("Magic sum:", magic_sum)

# Test the function with different sizes of magic squares
magic_square(3)
magic_square(4)
