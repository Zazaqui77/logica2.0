import os 

os.system("clear")  # limpar o terminal.

# Solicitando dados ( Entrada )
idade = int(input("Digite seu nome"))

# Verificando(Processamento)
# se idade < 18 entao
#     escreval ("Acesso Negado")
# fimse 

if idade < 18:
   print("Acesso negado!")
else: 
      print( "Acesso permitido!")


      # Exibindo dados 
print("==FIM==")