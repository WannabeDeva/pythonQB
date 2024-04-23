def is_palindrome(lst):
    # Compare the original list with its reverse
    return lst == lst[::-1]

# Example usage:
my_list1 = [1, 2, 3, 2, 1]
my_list2 = [1, 2, 3, 4, 5]

print("Is", my_list1, "a palindrome?", is_palindrome(my_list1))  # Output: True
print("Is", my_list2, "a palindrome?", is_palindrome(my_list2))  # Output: False
