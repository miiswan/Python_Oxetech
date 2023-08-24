# pça um valor entre 0 e 10,mostre uma mensagem caso o valor seja inválido e conitnue pedidno ate que o usuario insira um valor valido
nota = float(input('Insira uma nota entre zero e dez: '))

while (nota < 0 or nota > 10):
    print("Nota inválida!!!")
    nota = float(input("Insira um valor válido."))
    
print("Nota aceita com sucesso!")

