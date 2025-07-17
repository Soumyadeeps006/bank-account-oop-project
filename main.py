from bank_account import BankAccount

def main():
    print("Welcome to the Simple Bank!")
    owner = input("Enter account owner's name: ")
    initial_balance = float(input("Enter initial balance: "))
    
    account = BankAccount(owner, initial_balance)
    print(f"\nAccount created for {owner} with balance ${initial_balance:.2f}\n")

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Current balance: ${account.get_balance():.2f}")
        elif choice == "4":
            print("Thank you for using Simple Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()