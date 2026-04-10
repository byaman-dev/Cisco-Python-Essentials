# File: 05_weight_converter.py
# Objective: Convert KG to Lbs (1 kg = 2.20462 lbs).

kg = float(input("Enter weight in Kilograms: "))
pounds = kg * 2.20462

# Rounding to 2 decimal places for a clean look
print(kg, "kg is approximately", round(pounds, 2), "pounds.")
