def check_anagram(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)

# Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
if check_anagram(string1, string2):
    print("The strings '{}' and '{}' are anagrams.".format(string1, string2))
else:
    print("The strings '{}' and '{}' are not anagrams.".format(string1, string2))
