import csv
class ExpenseReport:
    def __init__(self):
        pass

    expenses = {
        "Food": [250, 180, 300],
        "Transport": [100, 60],
        "Entertainment": [500],
        "Bills": [1200]
    }

    def add_expense(self):
        category = input("Enter Category: ")
        amount = input("Enter Amount: $")
        self.expenses[category] = [int(amount)]
        print(self.expenses)

    def show_spending(self):
        total_expense=0
        self.cat_total_spend = {}
        for category,expense in self.expenses.items():
            spend_per_category = sum(expense)
            self.cat_total_spend[category] = spend_per_category
            total_expense+=spend_per_category
            print(f"Total Spend for {category} is ${spend_per_category}")
        print(f"Overall Spend is : ${total_expense}")
        #For each key, it calls the max function
        print(f"Highest Spent Category is {max(self.cat_total_spend.values())}")

    def export_to_csv(self):
        with open("expensereport.csv",mode="w") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Total Spend"])
            for cat,spend in self.cat_total_spend.items():
                writer.writerow([cat,spend])


expenseReport = ExpenseReport()
expenseReport.add_expense()
expenseReport.show_spending()
expenseReport.export_to_csv()
