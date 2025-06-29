def show_balance(balance):
    print(f"your balance is Rs.{balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposit: "))

    if amount < 0:
        print("Enter valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdrawn: "))
    
    if amount > balance:
        print("Your don't have enough balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdrawl")
        print("4.Exit")

        choice = input("Enter your choice(1-4): ")
        if choice=='1':
            show_balance(balance)
        elif choice =='2':
            balance += deposit()
        elif choice =='3':
            balance -= withdraw(balance)
        elif choice =='4':
            is_running = False
        else:
            print("Enter a valid choice")

    print("Thank you have a nice day")

if __name__ == "__main__":
    main()