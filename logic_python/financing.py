# Get the value of the house from the user
value = float(input("What is the value of the house? $"))
# Get the user's current salary
salary = float(input("What is your current salary? $"))
# Get the number of years for financing
time = float(input("How many years of financing? "))

# Calculate the monthly payment for the financing
financing = value / (time * 12)
# Calculate 30% of the salary as the minimum allowable monthly payment
minimum = salary * 30/100

print(
    f"With the value of ${value:.2f} and a salary of ${salary}, you will pay ${financing:.2f} per month to finance this house")

if financing <= minimum:
    # Print "Loan granted!" if the monthly payment is less than or equal to the minimum allowable payment
    print("Loan granted!")
else:
    # Print "Loan DENIED" if the monthly payment is greater than the minimum allowable payment
    print("Loan DENIED")
