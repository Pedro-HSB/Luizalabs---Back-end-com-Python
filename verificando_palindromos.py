palavra = input("Digite uma palavra: ").lower()

if palavra == palavra[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
