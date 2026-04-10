"""
Concept: Numeric Literals
Description: Understanding Scientific Notation, Hexadecimal, and Octal.
"""

# 1. Scientific Notation (e-notation)
# 3e8 means 3 * 10^8 (Speed of Light)
speed_of_light = 3e8 
small_number = 6.626e-34 # Planck's constant

print(f"Speed of Light: {speed_of_light} m/s")

# 2. Different Bases
# Binary (0b), Octal (0o), Hexadecimal (0x)
binary_val = 0b1010       # Decimal 10
hex_val = 0x1F            # Decimal 31

print(f"Binary 1010 is: {binary_val}")
print(f"Hex 1F is: {hex_val}")
