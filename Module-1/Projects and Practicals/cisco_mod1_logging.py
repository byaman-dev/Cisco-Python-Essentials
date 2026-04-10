# ==========================================================
# LAB: FORMATTED NETWORK REPORTING
# PURPOSE: Mastering the print() function for CLI output
# ==========================================================

# 1. BASIC OUTPUT
# Using \n for new lines and \t for tabbed alignment
print("System Status:\n\t- Firewall: ACTIVE\n\t- VPN: CONNECTED")

# 2. ADVANCED ARGUMENTS
# 'sep' defines the character between items.
# 'end' defines what happens at the end of the line (defaults to \n).
print("192", "168", "1", "1", sep=".") # Result: 192.168.1.1

# 3. CONCATENATION VS MULTIPLE ARGUMENTS
print("Analyzing " + "Packet " + "Data...")

# ==========================================================
# SECURITY TAKEAWAY:
# Consistent formatting is vital for Log Parsers. If your 
# AI model expects a '.' separator but receives a '-', the 
# security analysis will fail (Type Error).
# ==========================================================
