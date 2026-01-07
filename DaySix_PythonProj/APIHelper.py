import requests


class APIHelper:
    def __init__(self, country_name):
        self.country_name = country_name.strip()
        self.url = f"https://restcountries.com/v3.1/name/{self.country_name}?fullText=True"

    def get_country_data(self):
        try:
            response = requests.get(self.url, timeout=5)

            # 1️⃣ HTTP validation
            if response.status_code != 200:
                print(f"[ERROR] API failed for {self.country_name}")
                return None

            data = response.json()

            # 2️⃣ Data validation
            if not data or not isinstance(data, list):
                print(f"[ERROR] No data found for {self.country_name}")
                return None

            country = data[0]

            # 3️⃣ Key validation
            required_keys = ["name", "capital", "population", "region", "languages"]
            for key in required_keys:
                if key not in country:
                    print(f"[ERROR] Missing key '{key}' for {self.country_name}")
                    return None

            return {
                "country_name": country["name"]["official"],
                "capital": country["capital"][0],
                "population": country["population"],
                "region": country["region"],
                "languages": country["languages"]
            }

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Network issue for {self.country_name}: {e}")
            return None
