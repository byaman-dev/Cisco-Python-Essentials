# --- SECTOR 6: Type Casting & Interaction ---

# Scenario 1: Safe Type Conversion
user_input = "1024" 
buffer_size = int(user_input) # Converting string to integer for math

# Scenario 2: String Concatenation & Floating Point Precision
# Converting a float back to a string to display a message
risk_score = 0.856
print("System Threat Level: " + str(risk_score * 100) + "%")
