"""
Project: Student Budget & Savings Planner
Level: Class 11 / Cisco Module 2 Capstone
Objective: Synthesize all Module 2 concepts into a functional financial tool.
"""

def main():
    # --- 1. Header with String Replication ---
    print("=" * 40)
    print("   STUDENT FINANCIAL PLANNER v1.0   ")
    print("=" * 40)

    # --- 2. Data Acquisition (Input & Casting) ---
    name = input("Enter your name: ")
    monthly_allowance = float(input("Enter monthly allowance/income ($): "))
    expense_percent = float(input("Planned expense percentage (e.g., 70): "))

    # --- 3. Computational Logic (Arithmetic) ---
    # Calculate how much is spent and how much is saved
    spent_amount = monthly_allowance * (expense_percent / 100)
    savings_amount = monthly_allowance - spent_amount
    
    # Calculate a daily budget (assuming a 30-day month) using division
    daily_budget = spent_amount / 30

    # Using Modulo to see "Leftover" change if divided into $10 bills
    leftover_change = savings_amount % 10

    # --- 4. Professional Output Formatting ---
    print(f"\n--- Financial Summary for {name} ---")
    print(f"Total Allowance:  ${monthly_allowance:,.2f}")
    print(f"Monthly Expenses: ${spent_amount:,.2f} ({expense_percent}%)")
    print(f"Monthly Savings:  ${savings_amount:,.2f}")
    print("-" * 30)
    print(f"Suggested Daily Spend: ${daily_budget:,.2f}")
    print(f"Savings 'Loose Change' (under $10): ${leftover_change:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()
