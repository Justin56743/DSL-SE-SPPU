List_A = []
List_B = []

# Function to add students to List_A and List_B
def add_student(prn, dob):
  # Split the DOB into date and month
  date, month = dob.split("-")
  # Add the student information to the appropriate list based on the month of birth
  if int(month) < 6:
    List_A.append((prn, dob))
  else:
    List_B.append((prn, dob))

# Add some sample students to the lists
add_student("PRN001", "01-01")
add_student("PRN002", "02-03")
add_student("PRN003", "03-05")
add_student("PRN004", "04-07")
add_student("PRN005", "05-09")
add_student("PRN006", "06-11")
add_student("PRN007", "07-01")
add_student("PRN008", "08-03")
add_student("PRN009", "09-05")
add_student("PRN010", "10-07")

# Sort the lists based on DOB
List_A.sort(key=lambda x: x[1])
List_B.sort(key=lambda x: x[1])

# Merge the lists into List_SE_Comp_DOB
List_SE_Comp_DOB = List_A + List_B

# Print the merged and sorted list
print(List_SE_Comp_DOB)