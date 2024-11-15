
import sys
import os

# Adiciona o diretório raiz do projeto ao caminho de busca de módulos do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from login import Login
# from index import input_obrigatorio



class TestLogin(unittest.TestCase):
    def test_login(self):
        # Teste para IMC com valores normais
        login = Login()
        login.login('123')
        self.assertAlmostEqual(login.logado, True) 
            
    
    def test_login_invalido(self):
        # Verifica se a exceção ValueError é levantada quando a senha é incorreta
        with self.assertRaises(ValueError) as context:
            Login().login('321')  # Tentando fazer login com senha incorreta

        # Verifica se a mensagem da exceção é a esperada
        self.assertEqual(str(context.exception), "Senha incorreta!")
        
    def test_logout(self):
        login = Login()
        login.login('123')
        login.logout()
        self.assertAlmostEqual(login.logado, False)
    
if __name__ == "__main__":
    unittest.main()
