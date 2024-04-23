def multiplication_table(number):
    print("Multiplication table for", number, ":")
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

# Input number for which you want to create the multiplication table
input_number = int(input("Enter a number: "))

# Create and display the multiplication table
multiplication_table(input_number)
