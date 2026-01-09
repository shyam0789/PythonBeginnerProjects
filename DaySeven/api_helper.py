import requests

class APIHelper:
    def __init__(self, city_name):
      self.city_name = city_name
      self.api_key = "f14bcacaa80686cfd6a17fb53227b1ca"
      self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city_name}&APPID={self.api_key}"


    def get_weather_data(self):
        try:
            response = requests.get(url=self.url,timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception as ex:
             print("Invalid Response")
