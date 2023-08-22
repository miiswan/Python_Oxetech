# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Insira uma letra: "))

if (letra == 'A' or letra =='E' or letra == 'I' or letra == 'O' or letra == 'U'):
    print(f"Vogal.")
else:
    print(f"Consoante.")