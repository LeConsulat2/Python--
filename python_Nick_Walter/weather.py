import requests

try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=37.532600&lon=127.024612&appid=ec64b7b7b7049e1ab1aa4d5b00038afb")
    
except:
    print("No internet access, shame! 🤣")

response_json = response.json()

temp = response_json["main"] ["temp"]
temp_min = response_json["main"] ["temp_min"]
temp_max = response_json["main"] ["temp_max"]

print(f"In Seoul, it is currently {temp} C")
print(f"Today's high: {temp_min} C")
print(f"Today's low: {temp_max}° C")

#NOTE If you do like above, have to create all again, hence create class like below
class City:
    def __init__(self, city, lat, lon, units="metric" ):
        self.city = city
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=ec64b7b7b7049e1ab1aa4d5b00038afb")
    
        except:
            print("No internet access, shame! 🤣")

        response_json = response.json()

        self.temp = response_json["main"] ["temp"]
        self.temp_min = response_json["main"] ["temp_min"]
        self.temp_max = response_json["main"] ["temp_max"]


    def temp_print(self):
        print(f"In Auckland, it is currently {self.temp} C")
        print(f"Today's high: {self.temp_min} C")
        print(f"Today's low: {self.temp_max}° C")



my_city = City("Auckland", -36.848461, 174.763336)        
my_city.temp_print()