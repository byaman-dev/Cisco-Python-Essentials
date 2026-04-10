"""
Author: Aman (@byaman-dev)
Course: Cisco Python Essentials 1 - Module 1
Description: Demonstrating fundamental programming concepts: 
            Interpreters, Compilation, and Basic Instruction sets.
"""

# 1. The Print Function (The first instruction)
print("Cisco Python Essentials: Module 1 Complete!")

# 2. Demonstration of Python as an Interpreted Language
# Python executes code line-by-line. 
# If there was an error on line 20, lines 1-19 would still run.
print("Python is an interpreted language, meaning it's executed line-by-line.")

# 3. Basic Arithmetic (Instruction Processing)
# Computers process calculations using binary logic. 
# Here we test how the Python interpreter handles different operators:
print("Addition (2+2):", 2 + 2)
print("Multiplication (3*3):", 3 * 3)
print("Division (10/2):", 10 / 2) # Result is a 'float' (decimal)

# 4. Exploring 'End' and 'Sep' (Common Module 1 Lab tasks)
print("Programming", "is", "fun", sep="---") 
print("This is the end of the module", end="! ✅\n")

"""
Reflection: 
Module 1 taught me that Python code (.py) is converted into bytecode 
by the interpreter before being executed by the Python Virtual Machine (PVM).
"""
