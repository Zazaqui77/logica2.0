import os 

def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

numero_informado = int(input("Digite o numero da tabuada:"))
tabuada(numero_informado)


