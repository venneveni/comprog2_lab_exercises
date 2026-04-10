balance = 0
def current_balance():
    print(f"Current Balance: ₱{balance}")

def withdraw_money():
    global balance
    try:
        if not balance: 
            print("Your balance is ₱0. Please deposit money before attempting to withdraw.")
            return
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            balance -= amount
            print(f"Withdrawal successful. New balance: ₱{balance}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def deposit_money():
    global balance
    try:
        amount = float(input("Enter the amount to deposit:₱"))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            balance += amount
            print(f"Deposit successful. New balance: ₱{balance}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


while True:
    print("\n === Money Withdrawal System ==== ")
    print("\n 1. Deposit Money\n 2. Withdraw Money\n 3. Check Balance\n 4. Exit")
 
    try:
        choice = input("Enter your choice: ")

        if choice == '1':
            deposit_money()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            current_balance()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select only in the choiceses above.")
    except ValueError:
        print("Invalid input. Please enter a number.")
