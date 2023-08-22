# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

valor1 = float(input("Insira o valor: "))
valor2 = float(input("Insira o valor: ")) 
valor3 = float(input("Insira o valor: ")) 

if (valor1 < valor2 and valor1 < valor3):
    print(f"Compre o produto de valor {valor1}.")
elif (valor2 < valor1 and valor2 < valor3):
    print(f"Compre o produto de valor {valor2}.")
elif (valor3 < valor2 and valor3 < valor1):
    print(f"Compre o produto de valor {valor3}.")
