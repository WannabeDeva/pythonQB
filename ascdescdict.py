my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grapes': 3}

asc = dict(sorted(my_dict.items(), key= lambda item:item[1]))

desc = dict(sorted(my_dict.items(),key=lambda item:item[1], reverse=True))

print("Ascending Order:", asc)

print("Descending order:", desc)