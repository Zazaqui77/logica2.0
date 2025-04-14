import os

os.system("cls || clear")

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return f"O número {numero} é par."

    else:
        return f"O número {numero} é ímpar."

numero = int(input("Digite o número: "))
resultado = verificar_par_ou_impar(numero)
print(resultado)