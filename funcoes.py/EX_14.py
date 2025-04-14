import os

os.system("cls || clear")

def calcular_imc():
    peso = float(input("Digite seu peso (Kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    imc = peso / (altura ** 2)

    print(f"\nSeu IMC é: {imc:.2f}")

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        recomendado = "Tem que comer seu míseravel"
    
    elif imc < 25:
        classificacao = "Peso normal"
        recomendado = "Come saúdavel seu animal"

    elif imc < 30:
        classificacao = "Sobre peso"
        recomendado = "Comer menos e se exercicitar mais seu gordo"

    elif imc < 35:
        classificacao = "Obesidade grau 1"
        recomendado = "Procure orientção de um profissional"

    elif imc < 40:
        classificacao = "Obesidade grau 2"
        recomendado = "Procure orientção de um profissional"

    else:
        classificacao = "Obesidade grau 3"
        recomendado = "Busque assistência médica urgente"

    print(f"Classificação: {classificacao}")
    print(f"Recomendado: {recomendado}")

calcular_imc()
    
