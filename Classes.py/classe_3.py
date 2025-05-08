import os 
from dataclasses import dataclass

os.system("clas || clear")

@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = pessoa(
    nome = input("Digite o seu nome:"),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura= float(input("Digite sua altura:")),
    )

print()

pessoa2 = pessoa(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura = float(input("Digite sua altura: ")),
    )
 
print("\n=DADOS DA PESSOA =")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}, pesso: {pessoa1.peso}, altura: {pessoa1.altura}")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}, peso:{pessoa2.peso}, altura: {pessoa2.altura}")
