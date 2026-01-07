import json
from DaySix_PythonProj.UserInputHelper import UserInputHelper


class FileGenerator:
    def __init__(self):
        self.country_info = {}

    def create_json(self):
        user = UserInputHelper()
        user.get_user_input()
        self.country_info = user.get_data_from_api()
        with open("country_info.json",mode="w") as file:
            json.dump(self.country_info,file,indent=1)

    def list_comprehension(self):
       country_with_tamil = [country["country_name"] for country in self.country_info if "Tamil" in country["languages"].values()]
       print(f"Country with Tamil: {country_with_tamil}")
       country_with_pop_more_than_million = [country["country_name"] for country in self.country_info if country["population"]>100000000]
       print(f"Country with more than 10 crore: {country_with_pop_more_than_million}")

genFile = FileGenerator()
genFile.create_json()
genFile.list_comprehension()
