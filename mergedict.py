#method1

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge dict2 into dict1
dict1.update(dict2)

print("Merged dictionary:", dict1)

#method2

dict3 = {'a': 1, 'b': 2}
dict4 = {'c': 3, 'd': 4}

# Merge the dictionaries using dictionary unpacking
merged_dict = {**dict3, **dict4}

print("Merged dictionary:", merged_dict)

