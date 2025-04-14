import os
from datetime import date

os.system("clear || cls")

def calcular(data_nascimento):
    return date.today().year - data_nascimento

data_nascimento = int(input("Digite seu ano de nascimeto: "))

idade = calcular(data_nascimento)

print(f"Idade: {idade}")
