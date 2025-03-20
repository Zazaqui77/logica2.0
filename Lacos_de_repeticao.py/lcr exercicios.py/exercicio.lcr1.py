import os 
import time
os.system("cls || clear")

print("conatgem de 1 até 20 \nApenas ímpares:")
for i in range (1, 21):
    print(f"Número: {i}")

    print("conatgem de 1 até 20 \nApenas ímpares:")
for i in range (1, 21):
    if i % 2 == 1:
        print(f"Número: {i}")

numero = int(input("Digite o numero: "))
print(f"\nTabuada do número{numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um número para contagem regressiva: "))

print(f"\nIniciando contagem: ")
for i in range(numero,0, -1):
    print(f"{i}")
    time.sleep(1)



    