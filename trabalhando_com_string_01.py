nome = "PedRo H"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "      Hello World!         "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Slaaaa"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))


carros = ("gol")
print(isinstance(carros, tuple))


carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
carro.get("motor")
