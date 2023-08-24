# programa que leia um nome de usuario e sua senha e nao aceite a senha igual ao  nome do usuario, mostrando uma mensagem de erro e voltando a pedir as informacoes.

user = str(input("Insira seu nome de usuário: "))
senha = str(input("Insira sua senha: "))

while (user == senha):
    print(f"Usuário e senha iguais, tente novamente.")
    user = str(input("Insira seu nome de usuário: "))
    senha = str(input("Insira sua senha: "))
    
print(f"Usuário e senha aceitas.")    