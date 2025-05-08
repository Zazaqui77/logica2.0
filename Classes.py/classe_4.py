import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: str

class Endereco:
    logradouro: str
    numero: int

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso; {self.peso}")
        print(f"endereco: {self.endereco}, numero: {self.numero}")

endereco1 = Endereco("Rua A", 23)
pessoa1 = Pessoa("Marta", 25, endereco1)
pessoa1.exibir_dados()

print()

endereco2 = Endereco("Rua B", 47)
pessoa2 = Pessoa("João", 30 , endereco2 )
pessoa2.exibir_dados()
