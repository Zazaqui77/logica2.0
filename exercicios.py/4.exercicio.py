import os

os.system("Clear") # Limpar o terminal.

#Solicitando dados
usuario = "zazqui"
senha = "843"

usuario: input("Digite seu usario: ")  # type: ignore
senha: input("Digite sua senha: ")  # type: ignore

if usuario == usuario and senha == senha:
   print("Bem vindo !")
else:
   print("usario ou senha invalidos!")
