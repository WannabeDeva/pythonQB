

def count_odd_even(numbers):
    
    oddlist = []
    evenlist =[]

    for num in numbers:
        if num % 2 == 0:
            evenlist.append(num)
        else:
            oddlist.append(num)

    no_of_even = len(evenlist)
    no_of_odd = len(oddlist)

    return no_of_even, no_of_odd

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even, odd = count_odd_even(numbers)

print("No. of even numbers=",even)
print("No. of odd numbers=",odd)

