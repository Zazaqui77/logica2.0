import os 

os.system("clear") # limpar o teminal.

# Solicitando dados (Entrada)
idade = int(input("Digite sua idade: ")) 

# verificando(Processamento)
# se idade < 18 entao 
#       escreval("Acesso negado")
# fimse

if idade < 18:      
 print("Acesso negado!") 
else:  
  print("Acesso permitido!")



# Exibindo dados ( Saída )
print("== Fim ==")
