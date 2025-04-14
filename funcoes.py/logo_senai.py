import os 

def logo_senai():
    os.system("cls || clear ")
    print("=== SENAI ===")


logo_senai()
nome = input("Digite seu nome:")

logo_senai()
idade = input("Digite sua idade: ")

logo_senai()
print(f"\nNome: {nome}")
print(f"\nIdade: {idade}")