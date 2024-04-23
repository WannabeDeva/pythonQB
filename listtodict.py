def lists_to_dict(keys, values):
    # Use zip() to combine the two lists into pairs
    pairs = zip(keys, values)
    # Convert the pairs into a dictionary
    result_dict = dict(pairs)
    return result_dict

# Example usage:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = lists_to_dict(keys, values)
print("Mapped dictionary:", result)

