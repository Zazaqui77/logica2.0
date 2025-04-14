import os

os.system("cls || clear")

def somar(n1, n2):
    calcular = n1 + n2
    return calcular

def subtrair(n1, n2):
    calcular = n1 - n2
    return calcular

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = somar (n1, n2)
subtracao = subtrair(n1 , n2)
multiplicacao = multiplicar(n1 , n2)
divisao = dividir(n1, n2)

print(f"Soma: {soma}")
print(f"Subtrair: {subtrair}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisao: {divisao}")