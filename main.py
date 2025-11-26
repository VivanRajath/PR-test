# Simple ATM Machine Simulation

balance = 5000

print("===== Welcome to Python ATM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        print("Your Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful. New Balance:", balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. Remaining Balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using Python ATM")
        break

    else:
        print("Invalid choice")
