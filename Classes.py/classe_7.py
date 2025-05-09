import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Autor:
    nome_do_autor: str
    biografia: str
    nacionalidade: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor  # Corrigido para usar o tipo correto

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Ano: {self.ano}")
        print(f"Nome do autor: {self.autor.nome_do_autor}") 
        print(f"Biografia: {self.autor.biografia}")
        print(f"Nacionalidade: {self.autor.nacionalidade}")

# Criando instância de Autor
autor1 = Autor("Machado de Assis", "Foi um dos maiores escritores brasileiros do século XIX.", "Brasileiro")

# Criando instância de Livro com o autor
livro1 = Livro("Dom Casmurro", 1899, autor1)

# Exibindo os dados
livro1.exibir_dados()
