def reverse_sublist(lst, start, end):
    # Check if start and end indices are within the bounds of the list
    if start < 0 or end >= len(lst) or start >= end:
        return "Invalid indices"

    # Reverse the sublist using list slicing
    lst[start:end+1] = lst[start:end+1][::-1]

    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
start_index = 2
end_index = 5

# Reverse sublist from index 2 to 5
result = reverse_sublist(my_list, start_index, end_index)
print("Reversed list:", result)
