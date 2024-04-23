def digit_sum(n):
    # Base case: if the number is a single digit, return the number itself
    if n < 10:
        return n
    # Recursive case: add the last digit to the sum of the rest of the digits
    else:
        return n % 10 + digit_sum(n // 10)

# Input the non-negative integer
num = int(input("Enter a non-negative integer: "))

# Check if the input is non-negative
if num < 0:
    print("Please enter a non-negative integer.")
else:
    # Calculate and display the sum of digits
    print("Sum of digits:", digit_sum(num))
