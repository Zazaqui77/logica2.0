import os

os.system("cls || clear")


lista_numeros = []
quantidade = 6

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares



print(" = PAR  E IMPAR =")
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}° número: "))
    lista_numeros.append(numero)

pares, impares = pares_impares(lista_numeros)

print("\n= INTENS DA LISTA = ")
for i in enumerate(lista_numeros, start= 1):
    print(f"{i}: {numero}")

print(f"\nPares: {pares}")
print(f"Ìmpares: {impares}")