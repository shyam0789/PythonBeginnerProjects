# Minimum 8 characters
# At least:
# 1 uppercase letter
# 1 lowercase letter
# 1 number
# 1 special character (@#$!%&*)

class PasswordChecker:
    def __init__(self,password):
        self.password = password
        self.spl_char_list = ['(','@','#','$','!','%','&','*',')']
        self.has_upper = False
        self.has_lower = False
        self.has_number = False
        self.has_special = False
        self.has_eight_chars = False
        self.valid_password = False
        self.no_of_rules_met = 0
        self.present_dict = {
            "upper": "✔ Uppercase present",
            "lower": "✔ Lowercase present",
            "digit": "✔ Numbers present",
            "chars": "✔ Special chars present"
        }
        self.not_present_dict = {
            "upper": "X Uppercase missing",
            "lower": "X Lowercase missing",
            "digit": "X Numbers missing",
            "chars": "X Special chars missing"
        }
        self.output_dict = {}

    def check_password(self):
        if len(self.password) >=8:
            for s in self.password:
                if s.isdigit() and not self.has_number:
                    self.has_number = True
                    self.no_of_rules_met+=1
                if s.islower() and not self.has_lower:
                    self.has_lower = True
                    self.no_of_rules_met += 1
                if s.isupper() and not self.has_upper:
                    self.has_upper = True
                    self.no_of_rules_met += 1
                if s in self.spl_char_list and not self.has_special:
                    self.has_special = True
                    self.no_of_rules_met += 1
            self.valid_password =  (
                self.has_upper and
                self.has_lower and
                self.has_special and
                self.has_number)
            self.output_dict = {
                "upper": self.has_upper,
                "lower": self.has_lower,
                "digit": self.has_number,
                "chars": self.has_special
            }
        else:
            print("Password is less than 8 characters.")
        # print(f"Valid Password: {self.valid_password},No. of Rules: {self.no_of_rules_met}")
        return self.valid_password,self.no_of_rules_met

    def print_msg(self):
        false_keys = [k for k, v in self.output_dict.items() if v is False]
        true_keys =  [k for k,v in self.output_dict.items() if v is True]
        false_msg = [v for k,v in self.not_present_dict.items() if k in false_keys]
        true_msg = [v for k,v in self.present_dict.items() if k in true_keys]
        for msg in false_msg+true_msg:
            print(msg)
    # Alternate Way (Suggested)
    # def print_msg(self):
    #     for key, value in self.output_dict.items():
    #         if value:
    #             print(self.present_dict[key])
    #         else:
    #             print(self.not_present_dict[key])

password = input("Enter the password: ")
pwdCheck = PasswordChecker(password)
valid_password, no_of_rules_met = pwdCheck.check_password()

if no_of_rules_met in (1,2):
    print("Password Strength: Weak")
elif no_of_rules_met == 3:
    print("Password Strength: Medium")
elif no_of_rules_met == 4:
    print("Password Strength: STRONG")
pwdCheck.print_msg()
