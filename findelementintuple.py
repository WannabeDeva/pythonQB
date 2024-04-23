tuple_of_tuples = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

element = 'White'
element1 = 'Olive'
found = False

for tup in tuple_of_tuples:
    if element in tup:
        found = True
        break


print("Checking if " + element + "is in the list of tuples")
print(found)
