from datetime import datetime
from tkinter import *
import requests
import json

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
		resposta = resposta.strftime("%H:%M")

	return resposta



root = Tk()
temp = Label(root, text="Está fazendo " + jsonCall("temperatura") + " C°")
solPor = Label(root, text="O sol vai se por as: " + jsonCall("porSol"))
solNascer = Label(root, text="O sol vai nascer as: " + jsonCall("nascerSol"))
temp.pack()
solPor.pack()
solNascer.pack()
root.mainloop()