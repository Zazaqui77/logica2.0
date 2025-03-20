import os

os.system("cls || claer")

#solicitando dados
while True:
    
    nota1 = float(input("Digite a sua nota: "))
    
    if nota1 < 0 or nota1 > 10:
        print("Não aprovado.\n")
    else:
        break

while True:
    nota2 = float(input("Digite a sua nota: "))
    
    if nota2 < 0 or nota2 > 10:
        print("Não aprovado.\n")
    else:
        break

while True:
    nota3 = float(input("Dgite a sua nota:"))
    
    if nota3 < 0 or nota3 > 10:
        print("Não aprovado.\n")
    else:
        break

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"media: {media}")
print(f"Resultado: {resultado}")











Quantidade_notas = 2
soma = 0

for i in range(Quantidade_notas):
    while True:
        nota = float(input("Digite a {i+a}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota invalida.\n")
        else:
            soma += nota
            break
media = soma / Quantidade_notas

print(f"media: {media}")
 