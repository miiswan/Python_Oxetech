# faça um programa que peça onome de um usuário e depois peça o seu cpf e a  sua idade. ao final, imprima os 3 dados com um texto.

nome = str(input("Insira seu nome: "))
cpf = str(input("Digite seu número de CPF: "))
idade = int(input("Digite sua idade: "))

print(f"Olá {nome}, encontramos o seu cpf: {cpf}, no sistema. E verificamos que você tem {idade}.")