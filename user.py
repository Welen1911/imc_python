class User:
    def __init__(self, nome, email, telefone, idade, peso, altura):
        if (nome != None, idade != None, peso != None, altura != None):
            self.nome = nome
            self.email = email
            self.telefone = telefone
            self.idade = idade
            self.peso = peso
            self.altura = altura
            self.imc = None
            self.alerta = None
        else:
            raise ValueError("Nome, idade, peso e altura são obrigatórios!")

    def calcula_imc(self):
        if self.altura > 0:
            self.imc = float(self.peso) / (float(self.altura) ** 2)
        else:
            self.imc = None
        return self.imc

    def define_alerta(self):
        self.calcula_imc()
        
        if self.imc is None:
            self.alerta = "Dados inválidos"
        elif self.imc < 18.5:
            self.alerta = 'Abaixo do peso ideal'
        elif 24.9 < self.imc <= 29.9:
            self.alerta = 'Sobrepeso'
        elif 30 <= self.imc <= 34.9:
            self.alerta = 'Obesidade grau 1'
        elif self.imc > 35:
            self.alerta = 'Obesidade grau 2'
        else:
            self.alerta = None
        return self.alerta
