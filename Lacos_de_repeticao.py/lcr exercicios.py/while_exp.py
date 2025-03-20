import os

os.system("cls || clear")

#Exemplo de uso do laco de repeticao while.
while True:
    idade = int(input("Digite sua idade: "))
    
    if idade < 18:
        print("Não autorizado. \nSomente maiores de 18.\n")
    else:
        break

print("Acesso permitido")
print("Sesseção encerrada")
print("Fim")
