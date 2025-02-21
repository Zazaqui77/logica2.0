import os 
os.system ("clear")

#solicitar dados
Quantidade_macas=int(input("Quantidade de maçãs: "))
preco_por_maca=float(input("preço por maçã: " ))

#Caucule a media
if Quantidade_macas < 12:
    preco_por_maca= 1.30

else: 
    preco_por_maca= 1.00

custo_total= Quantidade_macas*preco_por_maca

#Mostrar na tela
print(f"o custo total da compra é: R${custo_total:.2f}")
