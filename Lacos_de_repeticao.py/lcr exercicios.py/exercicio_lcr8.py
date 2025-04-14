import os

os.system("cls || Clear")

contador = 0
soma_numeros = 0

while True:
    numero = int(input("Digite um número inteiro positivo (ou um negativo para sair): "))
    if numero < 0:
        break
    soma_numeros += numero
    contador += 1

if contador > 0:
    media = soma_numeros / contador
    print(f"A média dos números informados é: {media:.2f}")
else:
    print("Nenhum número válido foi inserido.")
