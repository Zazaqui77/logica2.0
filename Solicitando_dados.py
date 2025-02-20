import os

# Limpar o terminal.
os.system("clear")

# Solicitar dados para o usuário.
nome = input("Digite seu nome: ")
idade = int(input("Digite seu idade: "))
altura = float(input("Digite sua altura: "))           


# Exibindo dados.
print()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")

