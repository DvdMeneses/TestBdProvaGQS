from exames import *

import unittest

class TestExames(unittest.TestCase):

    def test_percentual_exames_alterados(self):
        # Casos de teste
        # 1- Dizer um exame e ter exames alterados
        # 2- Dizer um exame e não ter nenhum exame alterado
        # 3- Dizer um exame e não ter nenhum exame dele cadastrado

        # (id_medico, id_exame, data, resultado)

        situacao1 = [(1, 1, '5/2/22', 100), (1, 2, '5/2/22', 90), (2, 1, '4/9/21', 250)]
        # Exame id=1, valor_referencia=50
        r_esperado1 = 100
        # Exame id=1, valor_referencia=120
        r_esperado2 = 50
        # Exame id=1, valor_referencia=300
        r_esperado3 = 0
        # Exame id=3, valor_referencia=120
        r_esperado4 = 0
        # Exame id=2, valor_referencia=90
        r_esperado5 = 0

        self.assertEqual(percentual_exames_alterados(situacao1, 1, 50), r_esperado1)
        self.assertEqual(percentual_exames_alterados(situacao1, 1, 120), r_esperado2)
        self.assertEqual(percentual_exames_alterados(situacao1, 1, 300), r_esperado3)
        self.assertEqual(percentual_exames_alterados(situacao1, 3, 120), r_esperado4)
        self.assertEqual(percentual_exames_alterados(situacao1, 2, 90), r_esperado5)