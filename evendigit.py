def all_digits_even(number):
    for digit in str(number):
        if int(digit) % 2 != 0:
            return False
    return True

# Initialize an empty list to store the numbers
even_digit_numbers = []

# Iterate through each number between 100 and 400
for num in range(100, 401):
    # Check if all digits of the number are even
    if all_digits_even(num):
        even_digit_numbers.append(num)

# Print the numbers in a comma-separated sequence
print("Numbers between 100 and 400 where each digit is even:", ", ".join(map(str, even_digit_numbers)))

