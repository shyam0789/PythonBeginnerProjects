import json
class ExpenseStore:

    def write_expense(self,expense_list : list):
        with open("expenses.txt",mode="a") as file:
            file.write("\nDATE  |  CATEGORY  | TITLE  |  AMOUNT")
            for expense in expense_list:
                file.write(
                     f"\n{expense["transdate"]}  {expense["category"]}   {expense["expense_title"]}   {expense["amount"]}"
                 )
        with open("expenses.json",mode="a") as jsonfile:
            json.dump(expense_list[0],jsonfile,indent=4)





