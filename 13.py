def ternary_search(members, roll):
  # Set the initial boundaries of the search
  left = 0
  right = len(members) - 1

  # Perform the search
  while left <= right:
    # Calculate the three middle indices
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    # Check if the roll number is at one of the middle indices
    if members[mid1][0] == roll:
      return True
    if members[mid2][0] == roll:
      return True

    # Check which half of the list to search next
    if roll < members[mid1][0]:
      right = mid1 - 1
    elif roll > members[mid2][0]:
      left = mid2 + 1
    else:
      left = mid1 + 1
      right = mid2 - 1

  # If the roll number is not found, return False
  return False

# Test the function with a sample list of club members
members = [("R001", "Alice"), ("R002", "Bob"), ("R003", "Charlie"), ("R004", "Dave"), ("R005", "Eve")]
members.sort()
print(ternary_search(members, "R003"))  # Output: True
print(ternary_search(members, "R006"))  # Output: False
