
import sys
import os

# Adiciona o diretório raiz do projeto ao caminho de busca de módulos do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from user import User
# from index import input_obrigatorio



class TestIMC(unittest.TestCase):
    def test_calcula_imc(self):
        # Teste para IMC com valores normais
        user = User("João", "joao@example.com", "12345678", "25", 70, 1.75)
        imc = user.calcula_imc()
        self.assertAlmostEqual(imc, 22.86, places=2)  # Checa se o IMC está correto até 2 casas decimais
        
        # Teste para altura zero (deve retornar None)
        user = User("Maria", "maria@example.com", "87654321", "30", 60, 0)
        imc = user.calcula_imc()
        self.assertIsNone(imc)

    def test_define_alerta(self):
        # Teste para IMC abaixo do peso
        user = User("Ana", "ana@example.com", "98765432", "28", 45, 1.70)
        user.define_alerta()
        self.assertEqual(user.alerta, "Abaixo do peso ideal")
        
        # Teste para IMC de sobrepeso
        user = User("Carlos", "carlos@example.com", "76543210", "35", 80, 1.70)
        user.define_alerta()
        self.assertEqual(user.alerta, "Sobrepeso")
        
        # Teste para IMC de obesidade grau 1
        user = User("Beto", "beto@example.com", "123123123", "40", 90, 1.70)
        user.define_alerta()
        self.assertEqual(user.alerta, "Obesidade grau 1")

        # Teste para IMC de obesidade grau 2
        user = User("Paula", "paula@example.com", "321321321", "45", 120, 1.70)
        user.define_alerta()
        self.assertEqual(user.alerta, "Obesidade grau 2")

        # Teste para dados inválidos (altura zero)
        user = User("Pedro", "pedro@example.com", "123987123", "50", 70, 0)
        user.define_alerta()
        self.assertEqual(user.alerta, "Dados inválidos")

    
if __name__ == "__main__":
    unittest.main()
