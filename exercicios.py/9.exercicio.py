
import os 
os.system ("clear")

#solicitar dados
numero_um = int(input("Digite o numero um: "))
operacao_desejada= input("Digite a opereção desejada :")
numero_dois = int(input("Digite o numero dois: "))

#Vereficqando:
match operacao_desejada:
    case "-": 
        resultado= numero_um + numero_dois
    case "+":
        resultado= numero_um - numero_dois
    case "*":
        resultado= numero_um * numero_dois
    case "/":
        resultado= numero_um / numero_dois
case_:0
print("Opção inválida")


# Exibindo resultados

print()
print(f"primeiro número: {numero_um}")
print(f"operação: {operacao_desejada}")
print(f"segundo número: {numero_dois}")
print(f"resultado: {resultado}")
