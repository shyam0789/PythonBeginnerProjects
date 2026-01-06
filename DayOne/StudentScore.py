class Student:

    students = {
    "A": {"Math": 90, "Science": 85, "English": 88},
    "B": {"Math": 70, "Science": 65, "English": 72},
    "C": {"Math": 95, "Science": 98, "English": 92},
    "D": {"Math": 95, "Science": 100, "English": 95}
    }

    # Calculates:
    # Average score per student
    # Top scorer
    # Pass / Fail
    # status

    def cal_avg_score(self):
        for name,marks in self.students.items():
            avg = sum(marks.values())/len(marks)
            print(f"Average score of {name} is {avg}")
            if avg < 70:
                print(f"{name} has failed.")
            else:
                print(f"{name} has passed.")


    def topper(self):
        for name,marks in self.students.items():
            top_scorer = max(name for x in marks.values())
        print(f"Top Scorer is {top_scorer}")

student = Student()
student.cal_avg_score()
student.topper()

