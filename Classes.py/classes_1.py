import os 
from dataclasses import dataclass


os.system("cls || clear")

#Criando uma classe
@dataclass
class Pessoa:
    nome: str
    idade: int
#Aplicando características da classe.
pessoa1 = Pessoa("Alice", 30)
pessoa2= Pessoa("Bob", 25)

#Aplicando caracteerísteicas da classe.


print("\n= dados da pessoa =")
print(f"Nome: {pessoa1.nome} , idade: {pessoa1.idade} anos.")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} anos.")

