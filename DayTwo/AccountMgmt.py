class AccountManagement:

    def __init__(self):
        self.menu_dict = {
            1 : "Deposit",
            2 : "Withdraw",
            3 : "Check Balance",
            4 : "Transactions",
            5 : "Exit"
        }
        self.user_input = 0
        self.acc_bal = 0
        self.to_continue = True
        self.transactions = []

    def get_user_input(self):
        while self.to_continue:
            for key, value in self.menu_dict.items():
                print(f"{key}. {value}")
            self.user_input = int(input("Enter the option to proceed: "))
            if self.user_input == 1:
                amount = float(input("Enter the amount you wish to deposit: $"))
                self.deposit_money(amount)
            elif self.user_input == 2:
                amount = float(input("Enter the amount you wish to withdraw: $"))
                self.withdraw_money(amount)
            elif self.user_input == 3:
                self.check_balance()
            elif self.user_input == 4:
                self.display_transactions()
            elif self.user_input == 5:
                self.to_continue = False
                print("Thank you for using the Account Mgmt Service !")
            else:
                print("Invalid Input !. Input the values displayed in the menu.")


    def deposit_money(self,amount):
        self.acc_bal+=amount
        self.transactions.append(f"+{amount}")
        print(f"New A/c balance : ${self.acc_bal}")

    def withdraw_money(self,amount):
        if self.acc_bal < amount:
            print(f"Insufficient Balance !. Your a/c balance is ${self.acc_bal}")
        else:
            self.acc_bal -= amount
            self.transactions.append(f"-{amount}")
            print(f"Withdrawn amt: ${amount}. Your a/c balance is ${self.acc_bal}")

    def check_balance(self):
        print(f"Your a/c balance is: ${self.acc_bal}")

    def display_transactions(self):
        if self.transactions:
            print("Transactions")
            print("_" * 25)
            for items in self.transactions:
                print(items)
        else:
            print("No transactions to display.")



acct = AccountManagement()
acct.get_user_input()