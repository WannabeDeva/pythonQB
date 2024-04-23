def find_missing_numbers(set1, set2):
    # Find the missing numbers in set2 compared to set1
    missing_in_set2 = set1 - set2
    
    # Find the missing numbers in set1 compared to set2
    missing_in_set1 = set2 - set1
    
    return missing_in_set2, missing_in_set1

# Given sets of numbers
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find missing numbers
missing_in_set2, missing_in_set1 = find_missing_numbers(set1, set2)

# Display the result
print("Missing numbers in the second set compared to the first set:", missing_in_set2)
print("Missing numbers in the first set compared to the second set:", missing_in_set1)
