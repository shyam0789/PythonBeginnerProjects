import datetime as dt
from DayEight.expense_store import ExpenseStore as es

class ExpenseInput:
    def __init__(self):
        self.expense_title = ""
        self.category=""
        self.amount = 0.00
        self.transdate = ""
        self.expense_input_list = []

    def get_input(self):
        self.expense_title = input("Enter the Expense Title: ")
        self.category = input("Enter the Expense Category: ")
        self.amount = float(input("Enter the Expense: $"))
        self.transdate = input("Enter the Date of Txn (mm/dd/yyyy): ")

        if self.amount > 0 and  self.expense_title and self.category and self.validate_date():
            self.expense_input_list.append(
                {
                    "expense_title":self.expense_title,
                    "category" : self.category,
                    "amount":self.amount,
                    "transdate": self.transdate
                }
            )
            store = es()
            es.write_expense(store, self.expense_input_list)

    def validate_date(self):
        if dt.datetime.strptime(self.transdate,"%m/%d/%Y"):
            return True
        else:
            return False


expense_input = ExpenseInput()
expense_input.get_input()

