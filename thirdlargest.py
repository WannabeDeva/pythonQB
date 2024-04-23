def thirdlargest(numbers):
    unique_numbers = set(numbers)
    sorted_numbers = sorted(unique_numbers, reverse=True)
    if len(sorted_numbers)<3:
        print("There are less than three unique numbers")
    
    return sorted_numbers[2]

numbers = [10,10, 20, 30, 30, 40, 50]

third = thirdlargest(numbers) 

print("Given number list:")
print(numbers)

print("Third largest number:", third)