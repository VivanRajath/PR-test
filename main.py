import decimal
from decimal import Decimal

# Simple ATM Machine Simulation

# FIX: Use Decimal for financial calculations to prevent precision errors (Issue 6)
balance = Decimal('5000.00')

print("===== Welcome to Python ATM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = None
    while choice is None:
        try:
            user_input = input("Choose an option: ")
            choice = int(user_input)
            # Validate choice is within the menu range
            if not (1 <= choice <= 4):
                print("Invalid choice. Please enter a number between 1 and 4.")
                choice = None # Reset choice to re-enter
        except ValueError:
            # FIX: Existing try-except for choice input handles ValueError (Issue 1)
            print("Invalid input. Please enter a number (1-4).")

    if choice == 1:
        # FIX: Format balance to 2 decimal places for display
        print("Your Balance: ${:.2f}".format(balance))

    elif choice == 2:
        deposit_amount_valid = False
        while not deposit_amount_valid:
            try:
                amount_input = input("Enter amount to deposit: ")
                # FIX: Convert to Decimal instead of float (part of Issue 6, addresses Issue 2)
                amount = Decimal(amount_input)
                # FIX: Validate for positive deposit amount (Issue 3)
                if amount <= 0:
                    print("Deposit amount must be positive. Please enter a valid amount.")
                # Optional: Add an upper limit for deposit for robustness
                elif amount > Decimal('100000.00'):
                    print("Deposit amount exceeds maximum allowed (${:.2f}). Please enter a smaller amount.".format(Decimal('100000.00')))
                else:
                    balance += amount
                    print("Deposit successful. New Balance: ${:.2f}".format(balance))
                    deposit_amount_valid = True
            except decimal.InvalidOperation: # Catches non-numeric strings for Decimal conversion
                # FIX: Handle non-numeric input for deposit (Issue 2)
                print("Invalid input. Please enter a numerical amount.")
            except ValueError: # General fallback for other potential ValueErrors (e.g., empty string which Decimal might convert but int() would fail on if not handled)
                print("Invalid input. Please enter a numerical amount.")


    elif choice == 3:
        withdrawal_amount_valid = False
        while not withdrawal_amount_valid:
            try:
                amount_input = input("Enter amount to withdraw: ")
                # FIX: Convert to Decimal instead of float (part of Issue 6, addresses Issue 4)
                amount = Decimal(amount_input)

                # FIX: Validate for positive withdrawal amount (Issue 5)
                if amount <= 0:
                    print("Withdrawal amount must be positive. Please enter a valid amount.")
                # Optional: Add an upper limit for withdrawal for robustness
                elif amount > Decimal('10000.00'):
                    print("Withdrawal amount exceeds maximum allowed (${:.2f}). Please enter a smaller amount.".format(Decimal('10000.00')))
                elif amount > balance:
                    print("Insufficient balance. Your current balance is ${:.2f}".format(balance))
                else:
                    balance -= amount
                    print("Withdrawal successful. Remaining Balance: ${:.2f}".format(balance))
                    withdrawal_amount_valid = True
            except decimal.InvalidOperation: # Catches non-numeric strings for Decimal conversion
                # FIX: Handle non-numeric input for withdrawal (Issue 4)
                print("Invalid input. Please enter a numerical amount.")
            except ValueError: # General fallback for other potential ValueErrors
                print("Invalid input. Please enter a numerical amount.")

    elif choice == 4:
        print("Thank you for using Python ATM")
        break

    # The 'else: print("Invalid choice")' block is removed as the `while choice is None` loop
    # now guarantees that choice will be an integer between 1 and 4 before proceeding.