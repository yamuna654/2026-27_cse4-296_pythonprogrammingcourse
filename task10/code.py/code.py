
# ATM Menu-Driven Banking Simulation

balance = 5000.00

MIN_DEPOSIT = 100
MAX_DEPOSIT = 25000
MIN_WITHDRAWAL = 100
MAX_WITHDRAWAL = 10000
MIN_BALANCE = 500

transactions = []
total_deposits = 0.0
total_withdrawals = 0.0

while True:
    print("\n========== ATM MENU ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Exit")
    print("==============================")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: ₹"))

            if amount < MIN_DEPOSIT:
                print("Error: Minimum deposit is ₹100.")
            elif amount > MAX_DEPOSIT:
                print("Error: Maximum deposit is ₹25,000.")
            else:
                balance += amount
                total_deposits += amount
                transactions.append(
                    ("Deposit", amount, balance)
                )
                print(f"Deposit successful: ₹{amount:.2f}")
                print(f"Current balance: ₹{balance:.2f}")

        except ValueError:
            print("Error: Enter a valid numeric amount.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount < MIN_WITHDRAWAL:
                print("Error: Minimum withdrawal is ₹100.")
            elif amount > MAX_WITHDRAWAL:
                print("Error: Maximum withdrawal is ₹10,000.")
            elif balance - amount < MIN_BALANCE:
                print("Error: Insufficient balance.")
                print(f"Minimum balance required: ₹{MIN_BALANCE:.2f}")
            else:
                balance -= amount
                total_withdrawals += amount
                transactions.append(
                    ("Withdrawal", amount, balance)
                )
                print(f"Withdrawal successful: ₹{amount:.2f}")
                print(f"Current balance: ₹{balance:.2f}")

        except ValueError:
            print("Error: Enter a valid numeric amount.")

    elif choice == "3":
        print(f"Current account balance: ₹{balance:.2f}")

    elif choice == "4":
        print("\n====== TRANSACTION SUMMARY ======")

        if not transactions:
            print("No transactions have been made.")
        else:
            for number, transaction in enumerate(
                transactions, start=1
            ):
                transaction_type, amount, remaining = transaction

                print(
                    f"{number}. {transaction_type}: "
                    f"₹{amount:.2f} | "
                    f"Balance: ₹{remaining:.2f}"
                )

        print("---------------------------------")
        print(f"Total deposits:    ₹{total_deposits:.2f}")
        print(f"Total withdrawals: ₹{total_withdrawals:.2f}")
        print(f"Current balance:   ₹{balance:.2f}")
        print("=================================")

    elif choice == "5":
        print("\nThank you for using the ATM.")
        print(f"Final account balance: ₹{balance:.2f}")
        print("Session ended.")
        break

    else:
        print("Invalid choice. Please select an option from 1 to 5.")
