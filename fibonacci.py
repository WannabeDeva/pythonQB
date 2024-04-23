# Function to generate Fibonacci series up to a limit
def fibonacci_series(limit):
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]
    
    # Generate subsequent Fibonacci numbers until the limit is reached
    while True:
        # Calculate the next Fibonacci number by adding the last two numbers
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        
        # Check if the next Fibonacci number exceeds the limit
        if next_number > limit:
            break
        
        # Add the next Fibonacci number to the sequence
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence

# Get the Fibonacci series between 0 and 50
fibonacci_series_50 = fibonacci_series(50)

# Display the result
print("Fibonacci series between 0 and 50:", fibonacci_series_50)
