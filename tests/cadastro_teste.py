
import sys
import os

# Adiciona o diretório raiz do projeto ao caminho de busca de módulos do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from user import User
# from index import input_obrigatorio



class TestCadastro(unittest.TestCase):
    def test_cadastrar(self):
        # Teste para IMC com valores normais
        user = User("João", "joao@example.com", "12345678", "25", 70, 1.75)
        self.assertAlmostEqual(user.nome, 'João') 
        
        user = User(None, "joao@example.com", "12345678", "25", 70, 1.75)
    
    def test_cadastrar_invalido(self):
        user = User(None, "joao@example.com", "12345678", "25", 70, 1.75)

        user = User("João", "joao@example.com", "12345678", None, 70, 1.75)
        
        user = User("João", "joao@example.com", "12345678", "25", None, 1.75)

        user = User("João", "joao@example.com", "12345678", "25", 70, None)

        user = User(None, "joao@example.com", "12345678", None, None, None)


    
if __name__ == "__main__":
    unittest.main()
