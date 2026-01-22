class Country:

    def __init__(self):
        self.countries = []

    def get_data(self):
        self.countries = input("Enter the countries: ").split(",")
        # self.countries = [country in self.countries if not country]
        print(self.countries)





country = Country()
country.get_data()