def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal(n - 1)
        previous_row = triangle[-1]
        current_row = [1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row.append(1)
        triangle.append(current_row)
        return triangle

# Input handling
while True:
    try:
        n = int(input("Enter the number of rows for Pascal's triangle: "))
        if n >= 0:
            break
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Generate Pascal's triangle
result = pascal(n)

# Determine the maximum width required for centering
max_width = len(' '.join(map(str, result[-1])))

# Print Pascal's triangle as an equilateral triangle
for i, row in enumerate(result):
    row_str = ' '.join(map(str, row))
    print(row_str.center(max_width))

