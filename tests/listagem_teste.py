import sys
import os

# Adiciona o diretório raiz do projeto ao caminho de busca de módulos do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from io import StringIO
from user import User



class TestListarPessoas(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        "123", "João", "joao@example.com", "12345678", "25", "70", "1.75", 
        "S", "Maria", "maria@example.com", "98765432", "30", "60", "1.65", "n"
    ])
    def test_listar_pessoas(self, mock_input):
        # Definindo uma função para rodar o código principal
        pessoas = []
        password = input("Senha: ")

        if password == '123':
            while True:
                nome = input("Nome: ")
                email = input("E-mail: ")
                telefone = input("Telefone: ")
                idade = input("Idade: ")
                peso = input("Peso: ")
                altura = float(input("Altura: "))
                
                user = User(nome, email, telefone, idade, peso, altura)
                user.calcula_imc()
                pessoas.append(user)

                # Simula a pergunta de continuar
                res = input("Deseja continuar ? S/N")
                if res == 'n':
                    break

        # Verificando se as pessoas foram listadas corretamente
        self.assertEqual(len(pessoas), 2)  # Espera-se duas pessoas na lista
        self.assertEqual(pessoas[0].nome, "João")  # Verifica o nome da primeira pessoa
        self.assertEqual(pessoas[1].nome, "Maria")  # Verifica o nome da segunda pessoa

        # Simulando a impressão da lista de pessoas
        # Vamos capturar a saída impressa para verificar se a impressão está correta
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Imprime os cabeçalhos e os dados das pessoas
            print(f"{'Nome'.ljust(15)} {'Idade'.ljust(6)} {'Peso'.ljust(6)} {'Altura'.ljust(8)} {'IMC'.ljust(6)} {'Alerta'}")
            print('-' * 50)
            for pessoa in pessoas:
                print(f"{pessoa.nome.ljust(15)} {pessoa.idade.ljust(6)} {str(pessoa.peso).ljust(6)} {str(pessoa.altura).ljust(8)} {str(pessoa.imc).ljust(6)} {pessoa.alerta}")

            # Verificando se a impressão foi realizada corretamente
            output = mock_stdout.getvalue()  # Obtém o valor da saída capturada
            print("Output capturado:", output)

            # Verifica se o nome "João" está na saída
            self.assertIn("João".ljust(15), output)  # Verifica se o nome "João" está na saída
            self.assertIn("Maria".ljust(15), output)  # Verifica se o nome "Maria" está na saída

if __name__ == "__main__":
    unittest.main()
