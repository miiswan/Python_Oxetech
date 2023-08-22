# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = str(input("Insira a letra: "))

if (letra == 'F' or letra == 'f'):
    print(f"Sexo Feminino.")
elif (letra == 'M' or letra == 'm'):
    print(f"Sexo Masculino.")
else:
    print(f"Sexo Inválido.")