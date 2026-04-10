# --- SECTOR 4: Variables & Assignment Shortcuts ---

# Scenario 1: Defining System State
service_name = "Firewall_Alpha"
uptime_days = 12
is_active = True

# Scenario 2: Shortcut (In-place) Operators
# Updating a counter without rewriting the variable name
threat_count = 0
threat_count += 1  # Equivalent to threat_count = threat_count + 1
threat_count *= 2  # Doubling the value
print(f"Service: {service_name} | Current Threats: {threat_count}")
