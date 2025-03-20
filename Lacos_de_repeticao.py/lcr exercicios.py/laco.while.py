import os

os.system("cls || clear")

#Exemplo de uso do laco de repeticao while.
idade = int(input("Dgite sua idade: "))

while idade < 18:
    print("Não autorizado. \nSomente maiores de 18.\n")
    idade = int(input("Digite idade: "))

print("Acesso permitido")
print("Sesseção encerrada")
print("Fim")
