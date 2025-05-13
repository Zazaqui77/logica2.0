import os 
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Paciente:
    nome: str
    idade: int
    
    lista_pacientes = []

for i in range(2):
        print("Informe os dados do paiciente: ")
        paciente = Paciente(
        nome = input("Nome: "),
        idade = int(input("Idade: "))
        )

        Paciente.lista_pacientes.append(paciente)
        print("Paciente cadrastrado com sucesso !")

print("\n=DADOS DOS PACIENTES=")
for paciente in Paciente.lista_pacientes:
      print(f"Nome: {paciente.nome}")
      print(f"Idade: {paciente.idade}")
      print()
    
      print("= SALVANDO DADOS DOS PACIENTES =")
      nome_arquivo = "dado_paciente.txt"

with open(nome_arquivo, "w") as nome_arquivo:
      for paciente in paciente.lista_pacientes:
            nome_arquivo.write(f"Nome: {paciente.nome}\n")
            nome_arquivo.write(f"Idade: {paciente.idade}\n")
            nome_arquivo.write("\n")
            print("\n= SALVO COM SEUCESSO !")