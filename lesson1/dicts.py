cities = {"city": 'Moscow', "temperature": '20'}
print(cities["city"])
cities["temperature"] = str(int(cities["temperature"]) - 5)
print(cities)
print(cities.get("country"))
print(cities.get("country", 'Russia'))
cities["date"] = '27.05.2019'
print(len(cities))
print(cities)