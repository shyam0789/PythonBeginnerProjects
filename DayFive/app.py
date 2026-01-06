class VoteAgeValidatorForGit:

    def __init__(self,age):
        self.age = age

    def validate(self):
        if self.age < 18:
            print("Not Eligible to Vote")
        else:
            print("Eligible to Vote")