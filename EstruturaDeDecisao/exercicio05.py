# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Inira a nota 2:  "))
media = (nota1 + nota2) / 2

if (media >= 7):
    print(f"Sua média é igual a: {media}. Você está aprovado.")
elif (media == 10):
    print(f"Sua média é igual a 10. Você está aprovado com Distinção.")
else:
    print(f"Sua média é igual a: {media}. Você está reprovado.")
