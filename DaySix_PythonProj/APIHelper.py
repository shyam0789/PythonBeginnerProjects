import requests

class APIHelper:
    def __init__(self,countryName):
        self.countryName = countryName
        self.url = f"https://restcountries.com/v3.1/name/{self.countryName}?fullText=True"
        self.country_info = {}

    def get_country_data(self):
        print(self.url)
        response = requests.get(self.url)
        data = response.json()
        self.country_info = {
            "country_name":data[0]["name"]["official"],
            "capital": data[0]["capital"][0],
            "population": data[0]["population"],
            "region":data[0]["region"],
            "languages":data[0]["languages"]
        }
        return self.country_info


