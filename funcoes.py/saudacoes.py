import os
os.system("cls || clear")

def saudacao(nome):
    print(f"Olá {nome}! Bem - vindo(a) ao curso de DS!")
          

nome_visitante = "Marta"
saudacao(nome_visitante)

# Crie uma função com o nome: disciplina(nome) que receba o nome de 
# Uma disiciplina do curso de DS.
# Mostre o texto: A disciplina *** faz parte do curso de DS.
def disciplina (nome):
    print(f"A disciplina {nome}  faz parte do curso de DS.")

nome = input("Digite seu nome: ")
nome_disciplina = input("Digite o nome da disciplina: ")

saudacao("nome")# Chamando a função.
disciplina(nome_disciplina) # Chamando a função.