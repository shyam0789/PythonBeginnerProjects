import datetime
import json
import requests
class WeatherService:

    #Username : shyam_89
    #Pass: Mowni@us1

    def __init__(self):
        self.city = ""
        self.api_key = "f14bcacaa80686cfd6a17fb53227b1ca"
        #self.weather_url = "https://api.openweathermap.org/data/2.5/onecall?q="
        self.weather_url = f"https://api.openweathermap.org/data/2.5/weather?q=[0]&APPID={self.api_key}&units=metric"
        self.temperature=0
        self.humidity=""
        self.conditions=""
        self.data = []
    def get_data(self,city):
        self.city = city
        self.weather_url = self.weather_url.replace("[0]",city)
        data = requests.get(self.weather_url)
        response = data.json()
        self.temperature = response["main"]["temp"]
        self.conditions = response["weather"][0]["description"]
        self.humidity = response["main"]["humidity"]
        self.print_temp()
        self.add_to_json()

    def print_temp(self):
        print(f"Weather in {self.city}")
        print("_"*30)
        print(f"Temperature: {self.temperature}{'\u00b0'}c")
        print(f"Conditions: {self.conditions.title()}")
        print(f"Humidity: {self.humidity}%")


    def add_to_json(self):
        self.data.append({
            "city":self.city,
            "temp":self.temperature,
            "conditions":self.conditions,
            "humidity":self.humidity,
            "timestamp":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        })
        print(self.data)
        with open("weather.json",mode="a") as file:
             json.dump(self.data,file,indent=4)


ws = WeatherService()
city = input("Enter the City for which you need the weather for: ")
ws.get_data(city)


