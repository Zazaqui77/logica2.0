import os  

os.system ("Clear")


#solicitando dados

primeira_nota = float(input("Digite a nota da primeira unidade: "))
segunda_nota = float(input("Digite a nota da segunda unidade:"))
terceira_nota = float(input("Digite sua terceira nota: "))
media = float

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media < 7: 
    resultado = "Reprovado!"
else:
    resultado = "Aprovado!"

print(f"/nMédia:{media}")
print(f"Resultado: {resultado}")

