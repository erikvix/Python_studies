matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even_sum = third_col_sum = second_row_max = 0

# Populate the matrix and calculate the even sum
for row in range(0, 3):
    for col in range(0, 3):
        matrix[row][col] = int(
            input(f"Enter the value for row {row} and column {col}: "))
        if matrix[row][col] % 2 == 0:
            even_sum += matrix[row][col]

# Calculate the sum of the third column
for row in matrix:
    third_col_sum += row[2]

# Find the maximum value in the second row
for col in range(0, 3):
    if col == 0:
        second_row_max = matrix[1][col]
    elif matrix[1][col] > second_row_max:
        second_row_max = matrix[1][col]

# Print the matrix and the calculated values
print(f"""
{matrix[0]}
{matrix[1]}
{matrix[2]}
""")
print("-=" * 30)
print(f"The sum of the even numbers is {even_sum}")
print(f"The sum of the values in the third column is {third_col_sum}")
print(f"The highest value in the second row is {second_row_max}")
