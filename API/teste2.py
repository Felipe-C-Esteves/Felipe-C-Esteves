import json

y = input("número?")

temperatura = "a"
nuveins = "b"
nascerSol = "c"
porSol = "d"


def jsonCall(y):
    x = temperatura if y == "temperatura" else nuveins if y == "nuveins" else nascerSol if y == "nascerSol" else porSol if y == "porSol" else "imput invalido"
    return x

print(jsonCall(y))