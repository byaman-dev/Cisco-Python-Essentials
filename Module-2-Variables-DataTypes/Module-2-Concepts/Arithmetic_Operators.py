"""
Concept: Operators and Precedence
Description: A guide to +, -, *, /, //, %, and **
"""

x = 10
y = 3

print(f"Addition (10+3): {x + y}")
print(f"Standard Division (10/3): {x / y}")    # Returns a float
print(f"Integer Division (10//3): {x // y}")   # Returns 3 (rounds down)
print(f"Modulo (10%3): {x % y}")               # Returns 1 (the remainder)
print(f"Exponent (10^3): {x ** y}")            # 10 to the power of 3

# CONCEPT: PEMDAS (Order of Operations)
result = 2 + 3 * 5 ** 2
# 1. Power (5^2 = 25)
# 2. Multiply (3 * 25 = 75)
# 3. Add (2 + 75 = 77)
print(f"Result of 2 + 3 * 5 ** 2 is: {result}")
