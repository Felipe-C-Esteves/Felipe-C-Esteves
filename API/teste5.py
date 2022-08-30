import json

x = {
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 10000,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  }



#temperatura, nuveins, nascerSol, porSol
def jsonCall(y):
    resposta = json.dumps(x["main"]["temp"]) if y == "temperatura" else json.dumps(x["weather"][0]["description"]) if y == "nuveins" else json.dumps(x["sys"]["sunrise"]) if y == "nascerSol" else json.dumps(x["sys"]["sunset"]) if y == "porSol" else "input invalido"
    return resposta

pedido = input("Input: ")

if (pedido != "input invalido"):
  y = jsonCall(pedido)
else:
  print("pedido invalido")

print(y)