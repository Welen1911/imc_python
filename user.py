class User:
    nome = ''
    email = ''
    telefone = ''
    idade = None
    peso = None
    altura = None
    alerta = None
    imc = None

    def __init__(self, nome, email, telefone, idade, peso, altura):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def calc_imc(self):
        self.imc = float(self.peso) / (float(self.altura) ** 2)
        
        if (self.imc < 18.5):
            self.alerta = 'Abaixo do peso ideal'
        elif (self.imc > 24.9 and self.imc <= 29.9):
            self.alerta = 'Sobrepeso'
        elif (self.imc > 30 and self.imc <= 34.9 ):
            self.alerta = 'Obesidade grau 1'
        elif (self.imc > 35):
            self.alerta = 'Obesidade grau 2'
        if (self.alerta != None):
            print("\n" + "="*40)
            print(f"  ⚠️  AVISO: {self.alerta}  ⚠️")
            print("="*40 + "\n")

            