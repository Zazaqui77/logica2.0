import os

os.system("cls || Clear")

#Solicitando dados

contador = 0
soma_notas =0

while True:
    nota = float(input("Figite sua nota: "))
    soma_notas  += nota
    contador += 1

    continuar = input("Deseja inserir mais uma nota? (S/N): ").strip().upper()
    if continuar == 'N':

        if contador > 0:
            media = media = soma_notas / contador
            print(f"A média das notas é: {media:.2f}")
        else:
            print("Nehuma nota foi inserida.")