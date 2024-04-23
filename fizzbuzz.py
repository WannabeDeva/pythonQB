def fizz_buzz():
    for num in range(1, 51):  # Iterate from 1 to 50
        if num % 3 == 0 and num % 5 == 0:  # Check if the number is divisible by both 3 and 5
            print("FizzBuzz")
        elif num % 3 == 0:  # Check if the number is divisible by 3
            print("Fizz")
        elif num % 5 == 0:  # Check if the number is divisible by 5
            print("Buzz")
        else:
            print(num)  # If none of the above conditions are met, print the number

# Call the function to print Fizz, Buzz, or FizzBuzz
fizz_buzz()
