import os 
os.system ("clear")

#solicitar dados
numero_um = int(input("Digite o numero um: "))
numero_dois = int(input("Digite o numero dois: "))

#Caucule a media

soma=(numero_um + numero_dois)
produto=(numero_um*numero_dois) 
media=(numero_um + numero_dois)/2
menor=min(numero_um,numero_dois)
maior=max(numero_um,numero_dois)

# Exibir na tela 
print:() # type: ignore
print(f"Soma:  {soma}")
print(f"Produto:  {produto}")
print(f"Média: {media}")

if numero_um == numero_dois: 
   print(f"números são iguais")
else:
  print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

