def first_non_repeated_element(lst):
    # Create a dictionary to store the count of each element
    count_dict = {}

    # Count the occurrences of each element in the list
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    # Find the first element with count equal to 1
    for item in lst:
        if count_dict[item] == 1:
            return item

    # If no such element is found, return None
    return None

# Example usage:
my_list = [1, 2, 3, 2, 1, 4, 5]
result = first_non_repeated_element(my_list)
print("The first non-repeated element is:", result)
