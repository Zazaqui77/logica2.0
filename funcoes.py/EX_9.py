import os
os.system("cls || clear")

def preco_inflacionado(preco):
    if preco > 100:
      return  preco * 1.10
    
    else:
       return preco* 1.20
    
preco = float(input("Digte o preco: R$ "))

preco_final = preco_inflacionado(preco)

print(f"O preco final do produto é: R$ {preco_final:.2f}")