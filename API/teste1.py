
#lat e long vâo vir do GPS ou imput do usuario (fazer tabela de cidades)
#dar um jeito na chave (SEGURANÇA)
#mudar o tipo do pedido (weather, forecast, ets...)

def args(lat ,long, key):
    args = "https://api.openweathermap.org/data/2.5/weather?" + "lat=" + lat + "&lon=" + long + "&units=metric" + "&appid=" + key
    print(args)

args(input("qual é a latitude"), input("qual é a longitude"), input("Insira a chave da API"))
