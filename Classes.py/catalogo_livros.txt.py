import os 
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

# Lista de livros e quantidade definida fora da classe
lista_livros = []
QUANTIDADE_DE_LIVROS = 1

print("Informe os dados dos livros")
for i in range(QUANTIDADE_DE_LIVROS):
    livro = Livro(
        nome=input("Nome: "),
        autor=input("Autor: "),
        categoria=input("Categoria: "),
        preco=float(input("Preço: "))
    )
    lista_livros.append(livro)
    print()

print("\n=DADOS DOS LIVROS=")
for livro in lista_livros:
    print(f"Nome: {livro.nome}")
    print(f"Autor: {livro.autor}")
    print(f"Categoria: {livro.categoria}")
    print(f"Preço: R${livro.preco:.2f}")