def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    
    sum_of_digits = 0
    
    for digit in num_str:
        sum_of_digits = sum_of_digits + int(digit) * int(digit) * int(digit)  # Multiply the digit by itself twice
    
    return sum_of_digits == num

# Input the number to check
number = int(input("Enter a number: "))

# Check if the number is Armstrong
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
