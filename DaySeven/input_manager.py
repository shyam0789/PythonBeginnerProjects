from DaySeven.api_helper import APIHelper


class InputManager:

    def __init__(self):
        self.cities = []
        self.invalid_cities = []
        self.data = []

    def get_normalize_input(self):
        self.cities.append(input("Enter the Cities : "))
        self.cities = [city.strip() for city in list(filter(None, self.cities[0].split(","))) if city != ' ']
        print(self.cities)
        return self.cities

    def call_api(self):
        for city in self.cities:
            api_helper = APIHelper(city)
            self.data = api_helper.get_weather_data()
            print(self.data)





im = InputManager()
im.get_normalize_input()
im.call_api()
