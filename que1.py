#method1

list_of_tuple =  [(1, 2), (2, 3), (3, 4)]

list_of_lists = []

for tuple_item in list_of_tuple:
    convertedlist = list(tuple_item)
    list_of_lists.append(convertedlist)

print(list_of_tuple)

print(list_of_lists)

#method2
tuple_list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

lists_list = [list(t) for t in tuple_list]

print(tuple_list)

print(lists_list)