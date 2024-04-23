def count_digits_and_letters(string):
    # Initialize counters for digits and letters
    num_digits = 0
    num_letters = 0
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is a digit
        if char.isdigit():
            num_digits += 1
        # Check if the character is a letter
        elif char.isalpha():
            num_letters += 1
    
    return num_digits, num_letters

# Input the string
input_string = input("Enter a string: ")

# Calculate the number of digits and letters
digits, letters = count_digits_and_letters(input_string)

# Display the result
print("Number of digits:", digits)
print("Number of letters:", letters)
