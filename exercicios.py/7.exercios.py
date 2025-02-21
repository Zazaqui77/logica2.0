import os 

os.system("clear") # limpar o terminal.

#Solicitando dados 
primeiro_numero= int(input("Digite o primeiro número: ")) 
segundo_numero= int(input("Digite o segundo numero: "))
terceiro_numero= int(input("Digite o terceiro numero: "))

#Verificando maior ou menor
print(f" numeros indicados: {primeiro_numero}, {segundo_numero} e {terceiro_numero}")

#Determinar o maior e o menor
maior=max(primeiro_numero,segundo_numero,terceiro_numero)
menor=min(primeiro_numero,segundo_numero,terceiro_numero)



#exebir valor maior e menor 
print(f"maior numero:{maior}")
print(f"menor numero:{menor}")



