import os

os.system("Clear") # Limpar o terminal.

#Solicitando dados
idade = int (input("Digite sua idade : "))

#Verificando dados 

#opcão1

if idade >= 18 and idade <= 65:
    print("É obrigado a votar!")
else:
   print("Não é obrigado a votar!")