import os

os.system("cls || clear")

def verificar_positivo_ou_negativo(numero):
    if numero < 0:
        return f"O número {numero} é negativo."

    elif numero == 0:
        return f"O número 0 {numero} é néutro."
   
    else:
        return f"O número {numero} é positivo."  
    
    


numero = int(input("Digite o número: "))
resultado = verificar_positivo_ou_negativo(numero)
print(resultado)