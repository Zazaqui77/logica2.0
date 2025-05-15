import os
from dataclasses import dataclass

# Limpeza da tela (dependendo do sistema operacional)
os.system("cls" if os.name == "nt" else "clear")

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: str
    endereco: str

class Cliente:
    nome: str
    data_nascimento: str
    endereco: str

# Listas para armazenar os dados
lista_funcionario = []
lista_cliente = []

# Coleta de dados de Funcionários
print("Informe os dados do funcionario")
for i in range(3):
    funcionario = Funcionario(
        nome=input("Digite seu nome: "),
        data_admissao=input("Digite a sua data de admissão: "),
        matricula=input("Digite sua matricula: "),
        endereco=input("Digite seu endereço: ")
    )
    lista_funcionario.append(funcionario)
    print()

# Coleta de dados de Clientes
for i in range(3):
    cliente = Cliente(
        nome=input("Digite seu nome: "),
        data_nascimento=input("Digite sua data de nascimento: "),
        endereco=input("Digite seu endereço: ")
    )
    lista_cliente.append(cliente)
    print()

# Impressão dos dados dos Funcionários
print("\n=DADOS DOS FUNCIONÁRIOS=")
for funcionario in lista_funcionario:
    print(f"Nome: {funcionario.nome}")
    print(f"Data de Admissão: {funcionario.data_admissao}")
    print(f"Matricula: {funcionario.matricula}")
    print(f"Endereço: {funcionario.endereco}")

# Impressão dos dados dos Clientes
print("\n=DADOS DOS CLIENTES=")
for cliente in lista_cliente:
    print(f"Nome: {cliente.nome}")
    print(f"Data de Nascimento: {cliente.data_nascimento}")
    print(f"Endereço: {cliente.endereco}")
    print()

# Salvando dados dos Funcionários em arquivo
print("\n= SALVANDO DADOS DOS FUNCIONÁRIOS =")
nome_arquivo_funcionarios = "dados_funcionarios.txt"
with open(nome_arquivo_funcionarios, "w") as arquivo_funcionarios:
    for funcionario in lista_funcionario:
        arquivo_funcionarios.write(f"Nome: {funcionario.nome}\n")
        arquivo_funcionarios.write(f"Data de Admissão: {funcionario.data_admissao}\n")
        arquivo_funcionarios.write(f"Matricula: {funcionario.matricula}\n")
        arquivo_funcionarios.write(f"Endereço: {funcionario.endereco}\n")
        arquivo_funcionarios.write("\n")

print("= ARQUIVO FUNCIONÁRIOS SALVO COM SUCESSO !")

# Salvando dados dos Clientes em arquivo
print("\n= SALVANDO DADOS DOS CLIENTES =")
nome_arquivo_clientes = "dados_clientes.txt"
with open(nome_arquivo_clientes, "w") as arquivo_clientes:
    for cliente in lista_cliente:
        arquivo_clientes.write(f"Nome: {cliente.nome}\n")
        arquivo_clientes.write(f"Data de Nascimento: {cliente.data_nascimento}\n")
        arquivo_clientes.write(f"Endereço: {cliente.endereco}\n")
        arquivo_clientes.write("\n")

print("= ARQUIVO CLIENTES SALVO COM SUCESSO !")
