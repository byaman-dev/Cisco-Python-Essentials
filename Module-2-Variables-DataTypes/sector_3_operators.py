# --- SECTOR 3: Operators & Mathematical Expressions ---

# Scenario 1: High-Level Arithmetic
print("Exponentiation (2^10):", 2 ** 10) # Calculating 1024 (1KB)
print("Floor Division (15//4):", 15 // 4) # Returns the integer only

# Scenario 2: The Modulo Pattern (Cybersecurity Use Case)
# Using % to determine if a packet ID is even or odd for load balancing
packet_id = 4589
print(f"Packet ID {packet_id} is:", "Even" if packet_id % 2 == 0 else "Odd")
