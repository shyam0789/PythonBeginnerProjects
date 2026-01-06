import json
class TaskManager:

    def __init__(self):
        self.to_continue = True
        self.menu_dict = self.create_menu()
        self.user_input = 0
        self.id = 0
        self.task = []

    def display_menu(self):
        while self.to_continue:
            for key,value in self.menu_dict.items():
                print(f"{key}. {value}")
            self.user_input = int(input("Enter your option to proceed: "))

            if self.user_input == 1:
                self.add_task()
            elif self.user_input == 2:
                self.view_task()
            elif self.user_input == 3:
                self.id = int(input("Enter the Task ID: "))
                self.complete_task()
            elif self.user_input == 4:
                self.id = int(input("Enter the Task ID: "))
                self.delete_task()
            elif self.user_input == 5:
                self.save_task()
                self.to_continue = False

    def create_menu(self):
        return {
            1:"Add Task",
            2:"View Tasks",
            3:"Mark Task as Done",
            4:"Delete Task",
            5:"Save & Exit"
        }
    def add_task(self):
        title = input("Enter the title for the task: ")
        self.id = self.id+1
        new_task = {
            "id" : self.id,
            "title": title,
            "completed" : False
        }
        self.task.append(new_task)
    def view_task(self):
        symbol = ""
        for value in self.task:
            if value["completed"] : symbol = "[✔]"
            else: symbol = "[X]"
            print(f"{value["id"]}. {value["title"]} {symbol}")

    def complete_task(self):
        for item in self.task:
            if item["id"] == self.id: item["completed"] = True

    def delete_task(self):
        for item in self.task:
            if item["id"] == self.id:
                self.task.remove(item)
                break
    def save_task(self):
        with open("tasks.json",mode="w") as file:
            json.dump(self.task,file)

task = TaskManager()
task.display_menu()