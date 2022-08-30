import requests
import json

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={apikey}")
if response.status_code == 200:
    print("sucessfully fetched the data")
    y = response.json()
    print(json.dumps(y, indent=4))
else:
    print(f"there's a {response.status_code} error with your request")

print("Fim do programa")