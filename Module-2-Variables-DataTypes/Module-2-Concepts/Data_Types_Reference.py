"""
Concept: Python Data Types
Standard: Class 11 CS / Cisco Module 2.2
Description: Identifying and converting between different literal types.
"""

# 1. Integers (Whole numbers)
age = 17 

# 2. Floats (Decimals)
pi_value = 3.14159

# 3. Strings (Text)
name = "Gemini"

# 4. Booleans (Truth values)
is_student = True

print(f"Type of age: {type(age)}")
print(f"Type of pi: {type(pi_value)}")
print(f"Type of name: {type(name)}")
print(f"Type of is_student: {type(is_student)}")

# CONCEPT: Type Casting
# Converting a float to an int (removes decimals)
converted_pi = int(pi_value) 
print(f"Float {pi_value} cast to Int: {converted_pi}")
