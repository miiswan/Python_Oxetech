# Faça um programa que leia três números e mostre o maior deles.

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if (num1 > num2 and num1>num3):
    if(num2>num3):
        print(f"A ordem é: {num1}, {num2}, {num3}")
    else:
        print(f"A ordem é: {num1}, {num3}, {num2}")
