from DaySix_PythonProj.APIHelper import APIHelper


class UserInputHelper:
    def __init__(self):
        self.countries = []
        self.country_info = []

    def get_user_input(self):
        self.countries.append(input("Enter the Country name(s). "
                                     "Please enter countries as comma separated values: "))
        self.countries = self.countries[0].split(",")

    
    def get_data_from_api(self):
        for country in self.countries:
            apihelper = APIHelper(country)
            self.country_info.append(apihelper.get_country_data())
        return self.country_info




