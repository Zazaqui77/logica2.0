import os 

os.system("cls || clear")

#Solicitando dados
login_cadastrado = "Maiscaico"
senha_cadastrada = "banana123"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login_cadastrado == login and senha_cadastrada == senha:
        print(" Seja bem vindo!")
        break
    else:
        print("Acesso negado. \n Tente novamente\n")