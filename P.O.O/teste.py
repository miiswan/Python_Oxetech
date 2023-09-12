class Carro:
    def __init__(self,modelo,ano,cor,porta,motor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.porta = porta
        self.motor = motor
        self.ligado = False

    def __str__(self):
        return f"Modelo: {self.modelo}\nAno: {self.ano}"
    
    def acelerar(self):
        print(f"O {self.modelo} está acelerando! Vrum Vrum ")

    def frear(self):
        print(f"O {self.modelo} está freando! ")  

    def power(self):
        if self.ligado:
            print()

celta = Carro('celta',2010,'preto',4,1.0)
print(celta.porta)