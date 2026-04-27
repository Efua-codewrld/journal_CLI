import requests

API_KEY= "605c1b5d5ea7e261ab3c880491f8d948"

request= requests.get( "https://api.openweathermap.org/data/2.5/weather",params={"q" : "Accra", "appid" : API_KEY, "units" : "metric" })
data = request.json()
print(request.status_code)
print(data)

print(data["name"])
print(data["main"]["temp"])
print(data["weather"][0]["description"])