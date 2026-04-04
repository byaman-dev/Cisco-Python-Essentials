# --- SECTOR 1: The Print Function & Output Formatting ---

# Scenario 1: Using keyword arguments for clean logs
print("Status", "Online", "Secure", sep=" | ", end=" [OK]\n")

# Scenario 2: Professional Progress Tracking
# Using 'end' to simulate a real-time system update
print("Updating Database:", end=" ")
print("Loading", "Verifying", "Done", sep="...", end="!")
print("\n" + "="*30)
