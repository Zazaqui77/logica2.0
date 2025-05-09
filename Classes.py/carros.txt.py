import os 
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Carros:
    marca: str
    modelo: str
    categoria: str
    preco: float
   
listas_carros = []
QUANTIDADE_DE_CARROS = 4

print("Informe os dados dos carros")
for i in range(QUANTIDADE_DE_CARROS):
        carros = Carros(
        marca=input("marca:"),
        modelo=input("Email: "),
        preco=input("Telefone: "),
       categoria=input("categoria:")
        )
        
        listas_carros.append(carros)

print()

print("\n=DADOS DOS CLIENTES=")
for cliente in listas_carros:
    print(f"Marca: {Marca.nome}")
    print(f"Modelo:{cliente.email}")
    print(f"Preco: {cliente.telefone}")
    print()