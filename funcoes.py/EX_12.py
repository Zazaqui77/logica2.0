import os

os.system("cls || clear")

soma = 0

for i in range(3):
    nota = float(input(f"Digite sua nota {i + 1}: "))
    soma += nota

media = soma / 3
print(f"A média das 2 notas é: {media:.2f}")
