import requests
import json

def callApi():
	response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-22.25&lon=-45.7&units=metric&appid=5f3c395ff107f11834e93dbf0b6f8487")
	
	if response.status_code == 200:
		print("sucessfully fetched the data")
		clima = response.json()
		print(json.dumps(clima, indent=4))
		return str(clima["main"]["temp"]) + " C°"

	else:
		return f"there's a {response.status_code} error with your request"

print(callApi())
print("Fim do programa")