import os
from dataclasses import dataclass
os.system("Cls || clear")


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

listas_cliente = []
QUANTIDADE_DE_CLIENTES = 2

print("Informe os dados do cliente")
for i in range(QUANTIDADE_DE_CLIENTES):
    cliente = Cliente(
        nome =input("Nome:"),
        email=input("Email: "),
        telefone=input("Telefone: ")
     )
    listas_cliente.append(cliente)
    print()

print("\n=DADOS DOS CLIENTES=")
for cliente in listas_cliente:
    print(f"Nome: {cliente.nome}")
    print(f"Email:{cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print()

print("= SALVANDO DADOS DOS CLIENTES=")
nome_arquivo = "dado_clientes.txt"

#w -> escrita/salvar/sobrescrever
#a -> escrita/salvar/acumular

with open(nome_arquivo, "w") as arquivo:
    for cliente in listas_cliente:
        arquivo.write(f"Nome: {cliente.nome},{cliente.email},{cliente.telefone}\n")
        print("\n=Salvo com sucesso!")