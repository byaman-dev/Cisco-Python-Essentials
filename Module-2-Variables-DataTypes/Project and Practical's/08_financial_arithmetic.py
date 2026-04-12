"""
Module: Mathematical Data Processing
Practical: 02 - Financial Logic & Arithmetic Precedence
Objective: Implement high-precision fiscal calculations with robust error handling.
"""

# The function utilizes Type Hinting (float) to define expected numerical precision.
def calculate_transaction_final(subtotal: float, tip_rate: float) -> None:
    """
    Calculates total fiscal liability including gratuity.
    
    Technical Mechanism:
    - PEMDAS: Parentheses ensure (tip_rate / 100) executes before multiplication.
    - Exception Handling: The 'try' block isolates the calculation logic.
    - String Formatting: Utilizes f-string specifiers for currency display.
    """
    try:
        # Step 1: Calculate percentage as a decimal first for accuracy.
        # Step 2: Multiply by subtotal to find the monetary value of the tip.
        gratuity = subtotal * (tip_rate / 100)
        
        # Step 3: Perform addition to find the total liability.
        grand_total = subtotal + gratuity
        
        print(f"\n--- FISCAL AUDIT ---")
        
        # Format Logic: ':,.2f' 
        # ':' marks the start of formatting.
        # ',' adds thousand separators (e.g., 1,000).
        # '.2f' rounds the float to exactly 2 decimal places for financial standard.
        print(f"Subtotal: ${subtotal:,.2f}")
        print(f"Gratuity: ${gratuity:,.2f} ({tip_rate}%)")
        print(f"Total:    ${grand_total:,.2f}")

    # The 'except' block handles runtime anomalies.
    # Note: In a production environment, this prevents the application from 
    # crashing if a mathematical operation fails.
    except Exception as e:
        print(f"CRITICAL ERROR: Calculation failed. {e}")

# entry point for standalone script execution.
if __name__ == "__main__":
    
    # Nested Casting: We wrap input() inside float() to immediately transform
    # the default string data into a decimal-capable numeric type.
    try:
        amt = float(input("Enter Transaction Amount: "))
        rate = float(input("Enter Gratuity Percentage (e.g., 15): "))
        
        # Passing clean, casted data into the logic function.
        calculate_transaction_final(amt, rate)
        
    except ValueError:
        # This handles the specific error where a user types letters instead of numbers.
        print("INPUT ERROR: Please provide valid numerical values.")
