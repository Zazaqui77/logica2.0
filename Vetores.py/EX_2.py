import os

os.system("cls || clear")


lista_notas = []  # Criando uma lista
QUANTIDADE_NOTAS = 4
# Coletando 3 notas do usuário
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Calculando a média das notas
media = sum(lista_notas) / QUANTIDADE_NOTAS

if media >= 7:
    resultado = "Aprovado"

elif media >= 5:
    resultado = "Recuperação"
    
else:
    resultado = "Reprovado"
    
# Mostrando cada nota informada
print()
for nota in lista_notas:  # ForEach
    print(f"Nota: {nota}")

# Mostrando a média das notas
print()
print(f"Média: {media}")

# Mostrando apenas a segunda nota
print()
print(f"Somente a segunda nota: {lista_notas[1]}")