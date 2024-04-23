def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Input the number to check
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
