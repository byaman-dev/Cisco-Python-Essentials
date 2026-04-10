"""
Concept: Standard I/O (Input/Output)
Description: Mastering the print() and input() functions.
"""

# CONCEPT: Escape Characters
# \n = New line
# \t = Tab (space)
print("Line 1\nLine 2\t(Tabbed)")

# CONCEPT: Keyword Arguments
# 'end' changes what happens at the end of the line (default is \n)
print("Hello", end=" ")
print("World!") # This will stay on the same line as "Hello"

# CONCEPT: The Input Trap
# Remember: input() ALWAYS returns a string.
user_num = input("Enter a number: ")
print(f"Double the string: {user_num * 2}") # If input is 5, result is 55
print(f"Double the number: {int(user_num) * 2}") # If input is 5, result is 10
