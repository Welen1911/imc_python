from user import User

password = input(str('Senha: '))

if (password == '123'):


    nome = ""
    email = ""
    telefone = ""
    idade = None
    peso = None
    altura = None
    alerta = None

    pessoas = []


    def input_obrigatorio(value, msg, msgError):
        while True:
            value = input(str(msg))
            if value == "":
                print(msgError)
            else:
                return value


    while True:
        nome = input_obrigatorio(nome, "Nome: ", "Nome é obrigatório!")
        email = input(str("E-mail: "))
        telefone = input(str("Telefone: "))
        idade = input_obrigatorio(idade, "Idade: ", "Idade é obrigatório!")
        peso = input_obrigatorio(peso, "Peso: ", "Peso é obrigatório!")
        altura = input_obrigatorio(altura, "Altura: ", "Altura é obrigatório!")

        user = User(nome, email, telefone, idade, peso, altura)

        user.calc_imc()

        pessoas.append(user)

        print('Deseja continuar ? S/N')
        res = input(str(''))
        if res == 'n': break

    print(f"{'Nome'.ljust(15)} {'Idade'.ljust(6)} {'Peso'.ljust(6)} {'Altura'.ljust(8)} {'IMC'.ljust(6)} {'Alerta'}")
    print('-' * 50)
    for pessoa in pessoas:    
        print(f"{pessoa.nome.ljust(15)} {pessoa.idade.ljust(6)} {pessoa.peso.ljust(6)} {pessoa.altura.ljust(8)} {str(pessoa.imc).ljust(6)} {pessoa.alerta}")

