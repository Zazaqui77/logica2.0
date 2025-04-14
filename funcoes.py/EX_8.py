import os 
os.system("cls || clear")

def converter_centimetros(metros):
    return metros * 100

metros = float(input("Digite o valor: "))

centimetros = converter_centimetros(metros)

print("Tranformando em centimetros...")
print(f"O Resultado em centimetros é: {centimetros* 100:.2f}")


    