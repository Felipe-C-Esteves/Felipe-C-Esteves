import requests
import json
from datetime import datetime

def callApi():
	#inplementar a criação automatida da URL + esconder a chave da API
	response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-22.25&lon=-45.7&units=metric&appid=5f3c395ff107f11834e93dbf0b6f8487")

	if response.status_code == 200:
		print("sucessfully fetched the data")
		clima = response.json()
		return clima

	else:
		print(f"there's a {response.status_code} error with your request")


clima = callApi()

def jsonCall(y):
	#compara o input com as opções e retorna o valor correnspondente
	resposta = json.dumps(clima["main"]["temp"]) if y == "temperatura" else json.dumps(clima["weather"][0]["description"]) if y == "nuveins" else json.dumps(clima["sys"]["sunrise"]) if y == "nascerSol" else json.dumps(clima["sys"]["sunset"]) if y == "porSol" else "input invalido"
	
	#caso a resposta seja alguma data ou hora pasar de unix para utc
	if(y == "porSol" or y == "nascerSol"):
		resposta = datetime.fromtimestamp(int(resposta))
		resposta = resposta.strftime("%H:%M:%S")

	return resposta

pedido = input("Input: ")

print(jsonCall(pedido))


print("Fim do programa")