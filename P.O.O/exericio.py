class Aluno:
    def __init__(self,nome,idade,cpf):
        self.nome = nome 
        self.idade = idade 
        self.cpf = cpf 

    def __str__(self):
         return f"Nome: {self.nome} \nIdade: {self.idade} \nCPF: {self.cpf}"
    
    def verifica(self):
        if self.idade >= 18:
            print(f'o aluno é maior de idade.')
        else:
            print(f'O aluno é menor de idade.')

mirella = Aluno('Mirella',18,12555152498)
print(mirella)
