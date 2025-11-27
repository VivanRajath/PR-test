class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print(f"{amt} deposited")
        else:
            print("Invalid amount")

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print(f"{amt} withdrawn")
        else:
            print("Insufficient funds")

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name in self.accounts:
            print("Account already exists")
        else:
            self.accounts[name] = Account(name)
            print(f"Account created for {name}")

    def get_account(self, name):
        return self.accounts.get(name, None)

def main():
    bank = Bank()

    while True:
        print("\n1 Create Account")
        print("2 Deposit")
        print("3 Withdraw")
        print("4 Display")
        print("5 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            bank.create_account(name)

        elif choice == "2":
            name = input("Enter name: ")
            acc = bank.get_account(name)
            if acc:
                amt = float(input("Amount: "))
                acc.deposit(amt)

        elif choice == "3":
            name = input("Enter name: ")
            acc = bank.get_account(name)
            if acc:
                amt = float(input("Amount: "))
                acc.withdraw(amt)

        elif choice == "4":
            name = input("Enter name: ")
            acc = bank.get_account(name)
            if acc:
                acc.display()

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
