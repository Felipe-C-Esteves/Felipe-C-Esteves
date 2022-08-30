import requests
import json

def callApi():
	response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-22.25&lon=-45.7&units=metric&appid=5f3c395ff107f11834e93dbf0b6f8487")

	if response.status_code == 200:
		print("sucessfully fetched the data")
		clima = response.json()
		return clima

	else:
		print(f"there's a {response.status_code} error with your request")


x = callApi()

def jsonCall(y):
    resposta = json.dumps(x["main"]["temp"]) if y == "temperatura" else json.dumps(x["weather"][0]["description"]) if y == "nuveins" else json.dumps(x["sys"]["sunrise"]) if y == "nascerSol" else json.dumps(x["sys"]["sunset"]) if y == "porSol" else "input invalido"
	
    return resposta

pedido = input("Input: ")

if (pedido == "temperatura" or pedido == "nuveins"):
  y = jsonCall(pedido)
elif (pedido != "input invalido"):
  print("Converter para tempo normal")
  y = jsonCall(pedido)
else:
	y = "pedido invalido"

print(y)


print("Fim do programa")

#þussy