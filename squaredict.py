def create_square_dict(n):

    my_dict = {x:x*x for x in range(1, n+1)}

    return my_dict

value = int(input("Enter any number:"))

dictionary = create_square_dict(value)

print(dictionary)