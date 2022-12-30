def radix_sort(arr, d):
    # Create a list of empty queues
    queues = [[] for _ in range(10)]

    # Distribute the elements of the array into the queues based on the value of their d-th digit
    for x in arr:
        digit = (x // (10 ** (d-1))) % 10
        queues[digit].append(x)

    # Concatenate the queues to obtain the sorted array
    sorted_arr = []
    for queue in queues:
        sorted_arr.extend(queue)
    
    return sorted_arr

def radix_sort_helper(arr, d):
    if d == 0:
        return arr
    else:
        return radix_sort_helper(radix_sort(arr, d), d-1)

# Array of 10th class percentages of students
percentages = [65.5, 75.3, 82.1, 56.7, 88.2, 91.8, 74.4, 60.6, 55.5, 79.7]

# Determine the maximum number of digits in the percentages
max_digits = len(str(int(max(percentages))))

# Sort the array using radix sort
sorted_percentages = radix_sort_helper(percentages, max_digits)

# Display the top five scores
print("Top five scores:")
for i in range(5):
    print(sorted_percentages[i])
