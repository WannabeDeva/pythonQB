#method1

list_of_tuples = [(1, 2), (2, 3), (3, 4)]

sum_of_elements = []

for tuple_item in list_of_tuples:
    sum_tuple = sum(tuple_item)
    sum_of_elements.append(sum_tuple)

print(list_of_tuples)

print(sum_of_elements)

#method2

tuple_list = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

sum_list = [sum(t) for t in tuple_list]

print(tuple_list)

print(sum_list)