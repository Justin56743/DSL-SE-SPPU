def bucket_sort(arr):
    # Create a list of empty buckets
    buckets = [[] for _ in range(len(arr))]
    
    # Distribute the elements of the array into the buckets
    for x in arr:
        bucket_index = int(len(arr) * x)
        buckets[bucket_index].append(x)
    
    # Sort the elements in each bucket
    for bucket in buckets:
        bucket.sort()
    
    # Concatenate the sorted buckets to obtain the sorted array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Array of 12th class percentages of students
percentages = [65.5, 75.3, 82.1, 56.7, 88.2, 91.8, 74.4, 60.6, 55.5, 79.7]

# Sort the array using bucket sort
sorted_percentages = bucket_sort(percentages)

# Display the top five scores
print("Top five scores:")
for i in range(5):
    print(sorted_percentages[i])
