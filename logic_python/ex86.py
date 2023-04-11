# Create an empty list with two sub-lists to store even and odd numbers.
list = [[], []]

# Iterate seven times to collect seven numbers from the user.
for c in range(0, 7):
    # Prompt the user to enter a number and convert it to an integer.
    value = int(input(f"Enter the {c+1} number: "))
    if value % 2 == 0:  # Check if the value is even.
        list[0].append(value)  # If so, add it to the first sub-list (list[0]).
    elif value % 2 == 1:  # Check if the value is odd.
        # If so, add it to the second sub-list (list[1]).
        list[1].append(value)

# Print the even values entered by the user.
print(f"The even values entered were {list[0]}")
# Print the odd values entered by the user.
print(f"The odd values entered were {list[1]}")
