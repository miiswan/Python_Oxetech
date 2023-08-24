# Supondo que a populaçao de um país A seja da ordem de 8000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B mantidas as taxas de crescimento.

# A = 80000 - 3% por ano 
# B = 200000 - 1.5% por ano

a = 80000
b = 200000
ano = 0

while(a<b):
    a += a * 0.03
    b += b * 0.015
    ano +=1
    print
print(f"A população do pais A passou em {ano} anos")