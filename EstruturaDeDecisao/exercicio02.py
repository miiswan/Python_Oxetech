# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

value = int(input("Insira um valor: "))

if (value > 0):
    print(f"O valor é positivo.")
elif (value == 0):
    print(f"O valor é nulo.")
else:
    print(f"O valor é negativo.")