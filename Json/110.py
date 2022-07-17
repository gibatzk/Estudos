import json

x = {
    "nome":"Gilberto",
    "idade":36,
    "casado":True,
    "divorciado":False,
    "filho":None,
    "pet":"Robin",
    "carro": [
        {"modelo":"fiat Fiorino", "cor":"branca"},
        {"modelo":"Peuget 504", "cor":"preta"}
    ]
}

#print(json.dumps(x, indent=4))
#print(json.dumps(x, indent=4, separators=(". ", " = ")))
#y = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)
y = json.dumps(x, separators=(". ", " = "), sort_keys=True)


print(y)
