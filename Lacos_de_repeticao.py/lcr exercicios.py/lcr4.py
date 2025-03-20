import os

os.system("cls || clear")

divisao = 0 

for i in range(4):
    media= int(input("Digite um numero: "))
    divisao += media
    media_total = divisao / 4 
print(f"sua media totoal foi: {media_total:.2f}")