import os
from dataclasses import dataclass
os.system("cls || claer")

#criando uma classe
@dataclass
class Pet:
    nome: str
    idade: int
    peso: float
    #Aplicando características da classe>

pet1 = Pet("Totó", 4, 7.8)
pet2 = Pet("Tuburão", 6,9.2)

print("\n= dados d pet =")
print(f"Nome: {pet1.nome}, idade:{pet1.idade}, peso: {pet1.peso}")
print(f"Nome: {pet2.nome}, iade: {pet2.idade}, peso: {pet2.peso}")