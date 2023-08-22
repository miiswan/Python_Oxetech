# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 > num2 and num1 > num3 and num3 > num2):
    print(f"O número {num1} é o maior e o {num2} é o menor entre eles.")
elif (num1 > num2 and num1 > num3 and num2 > num3):
    print(f"O número {num1} é o maior e o {num3} é o menor entre eles.")
elif (num2 > num1 and num2 > num3 and num3 > num1):
    print(f"O número {num2} é o maior e o {num1} o menor entre eles.")
elif (num2 > num1 and num2 > num3 and num1 > num3):
    print(f"O número {num2} é o maior e o {num3} o menor entre eles.")
elif (num3 > num1 and num3 > num2 and num2 > num1):
    print(f"O número {num3} é o maior e o {num1} o menor entre eles.")
else:
    print(f"O número {num3} é o maior e o {num2} é o menor entre eles.")