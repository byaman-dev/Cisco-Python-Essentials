"""
Concept: Bitwise Operators (Basics)
Description: Manipulating data at the bit level.
"""

a = 6  # In binary: 110
b = 3  # In binary: 011

# AND (&) - 1 only if both bits are 1
# 110 & 011 = 010 (Decimal 2)
print(f"Bitwise AND (6 & 3): {a & b}")

# OR (|) - 1 if at least one bit is 1
# 110 | 011 = 111 (Decimal 7)
print(f"Bitwise OR (6 | 3): {a | b}")

# Shift Operators (Moving bits left or right)
# 6 << 1 shifts bits left (effectively multiplying by 2)
print(f"Bitwise Left Shift (6 << 1): {a << 1}")
