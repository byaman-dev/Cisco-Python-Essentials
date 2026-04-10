"""
Concept: String Manipulation Operators
Description: Using + and * with string literals.
"""

# 1. Concatenation (+) - Joining strings
greeting = "Hello" + " " + "Student"
print(greeting)

# 2. Replication (*) - Repeating strings
# This is very useful for creating dividers in console apps
border = "=" * 30
print(border)
print("ACADEMIC REPORT")
print(border)

# 3. Mixing Types (The Error Trap)
# print("Age: " + 17)  <-- This will cause a TypeError
print("Age: " + str(17)) # Correct way: Cast number to string first
