import os 
os.system("cls || clear")

lista_compras = []
QUANTIDADE = 3

print("Lista de compras =")
for i in range(QUANTIDADE):
    item = input("Digite {i + 1}º item para lista")
    lista_compras.append(item)

#Exibindo resultados
print("\nitem da lista=")
for i, item in enumerate (lista_compras, start=1):
    print(f"{i}º item: {item}")