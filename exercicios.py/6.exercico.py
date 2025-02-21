import os

os.system("Clear") # Limpar o terminal.

#Solicitando dados
idade = int (input("Digite sua idade : "))

#Verificando dados 

#opcão1

if idade < 18 or idade > 65:
    print("É obrigado a votar!")
if idade > 16 and idade < 17 or 65:
    print("Voto opcional")
if idade > 18:
    print("Não é opicional")    
