# File: 04_swap_variables.py
# Objective: Swap two numbers using arithmetic instead of a temporary variable.

a = int(input("Enter A: ")) # Example: 5
b = int(input("Enter B: ")) # Example: 10

# Logic
a = a + b # a becomes 15
b = a - b # b becomes 15 - 10 = 5
a = a - b # a becomes 15 - 5 = 10

print("After Swapping -> A:", a, "B:", b)
