import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Carro:
    marca: str
    modelo: str
    categoria: str
    preco: float

listas_carros = []
QUANTIDADE_DE_CARROS = 2

print("Informe os dados dos carros")
for i in range(QUANTIDADE_DE_CARROS):
    print(f"\nCarro {i + 1}:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    
    # Validação de preço
    while True:
        try:
            preco = float(input("Preço: "))
            break
        except ValueError:
            print("Erro: Digite um número válido para o preço (ex: 50000 ou 49999.99).")

    categoria = input("Categoria: ")

    carro = Carro(marca=marca, modelo=modelo, preco=preco, categoria=categoria)
    listas_carros.append(carro)

print("\n=DADOS DOS CARROS=")
for i, in enumerate(listas_carros, star=1):
    print(f"Marca: {carro.marca}")
    print(f"Modelo: {carro.modelo}")
    print(f"Preço: R${carro.preco:.2f}")
    print(f"Categoria: {carro.categoria}")
    print("-" * 20)
