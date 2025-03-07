import os 
os.system ("clear")

#solicitar dados
print("""
====================MENU===============
Codigo     \tPrato     \t\tValor
1   \t\tPicanha     \t\t25,00   
2   \t\tLasanha     \t\t20,00
3   \t\Strogonoff   \t\t18,00
4   \t\Latiifa virg \t\t60,00
5   \t\Macaco ass   \t\t100,00
6   \t\Rato frito   \t\t80,00

   
""")

opcao = int (input("Digite a opção desejada: "))

match opcao:
    case 1:
        Prato= "Rato frito"  
        Valor= 80
    case 2:
        Prato= "Macaco ass"
        Valor: 100
    case 3:
        Prato= "Picanha"
        Valor= 25
    case _:
        Prato= "Opção inválida"
print()
print(f"Prato:{Prato}")
print(f"valor: R$ {Valor:.2f}")