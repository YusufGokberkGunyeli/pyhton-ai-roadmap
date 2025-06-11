balance = 1000
def show_menu():
    print("\nWelcome to Yusufbank atm")
    print("1 - Show Balance")
    print("2 - Deposit Money")
    print("3 - Withdraw Money")
    print("4 - Exit")

def show_balance():
    print(f"Your current balance is: {balance} dolars")

def deposit_money():
    global balance
    amount = float(input("Please enter how much money do you wante to deposit: "))
    balance += amount
    print(f"{amount} dolars deposited")

def withdraw_money():
    global balance
    amount = float(input("Please enter how much money you want to withdraw: "))
    if amount < balance:
        balance -= amount
        print(f"{amount} dolars withdrawn please take your card")
    else:
        print("You dont have balance for that")
        show_balance()

def exit_atm():
    print("Thank you for chosing Yusufbank have a great day :)")

while True:
    show_menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        show_balance()
    elif choice == 2:
        deposit_money()
    elif choice == 3:
        withdraw_money()
    elif choice == 4:
        exit_atm()
    else:
        print("Invalid option :( ")