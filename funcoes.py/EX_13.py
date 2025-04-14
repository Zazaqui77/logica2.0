import os

os.system("cls || clear")

soma = 0

for i in range(2):
    nota = float(input(f"Digite sua nota {i + 1}: "))
    soma += nota

media = soma / 2
print(f"A média das 2 notas é: {media:.2f}")

if media >= 7:
    print("Aprovado !")

elif media >= 6:
    print("Recuperação !")

else:
    print("Reprovado !")