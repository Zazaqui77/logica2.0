import os 
os.system("cls || clear")

numeros = []

qunatidade = int(input("QUantos números você quer armazenar ?: "))

for i in range(5):
    numero = float(input(f"Digite o {i + 1 }º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

if numeros:
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"\nnmueros informados:" , numeros )
for n in numeros:
    print(n)


print(f"\nmaior número: {maior}")
print(f"\nmenor número: {menor}")


