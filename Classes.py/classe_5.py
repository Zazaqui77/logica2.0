import os 
from dataclasses import dataclass
os.system("Clas || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float
@dataclass
class Endereco:
    logradouro: str
    endereco: str
    numero: int

Pessoa1 = Pessoa(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    altura = float(input("Digite sua altura: "))
    )

print()

Endereco1 = Endereco(
    logradouro = input("Digite seu endereco: "),
    endereco = input("Digite o nome da sua rua: "),
    numero = int(input("Digite o numero da sua rua: "))
    )

print("\n=DADOS DA PESSOA =")
print(f"Nome: {Pessoa1.nome}, Idade: {Pessoa1.idade}, Altura: {Pessoa1.altura}")
print(f"Endereco: {Endereco1.logradouro}, Endereco: {Endereco1.endereco}, Numero:{Endereco1.numero}")