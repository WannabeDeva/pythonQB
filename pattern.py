def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="\t")
        print()

# Number of rows in the pattern
num_rows = 5

# Print the pattern
print_pattern(num_rows)
