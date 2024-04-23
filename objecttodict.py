#method1

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

insaan = Person("Deva", 20)

my_dict = vars(insaan)

print(my_dict)

#method2

my_dict2 = insaan.__dict__ 

print(my_dict2)