# File: 02_simple_interest.py
# Objective: Financial calculation using user input.

principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
time = float(input("Enter Time (years): "))

interest = (principal * rate * time) / 100

print("The Simple Interest is:", interest)
print("Total Amount to pay:", principal + interest)

