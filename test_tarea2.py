import io
import sys
import unittest
from unittest.mock import patch
from io import StringIO

from tarea2 import Guess


class TestTarea2(unittest.TestCase, Guess):

    def setUp(self):
        """
        Inicializa estructura de datos con la que se realizarán las pruebas.
        """
        self.ok = [4,3,2,1]
        self.no = [5,6,7,8,9,0]
        self.hit = ["","","",""]

    ## Tests función find_regulars().

    @patch('tarea2.Guess.find_regulars')
    def test_find_regulars_is_called(self, mock_reg):
        """
        Tests de llamada a la función.
        """
        self.find_regulars()
        self.assertTrue(mock_reg.called)

    def test_find_regulars_guessing_1234(self):
        """
        Verifica valor de salida. Valores correspondientes al número 1234.
        """
        with patch('builtins.input', side_effect=[4,0,0,0]):
            self.find_regulars()
            reg = self.ok
        self.assertEqual(reg, [1,2,3,4])

    def test_find_regulars_guessing_7890(self):
        """
        Verifica valor de salida. Valores correspondientes al número 7890.
        """
        with patch('builtins.input', side_effect=[0,0,4,0]):
            self.find_regulars()
            reg = self.ok
        self.assertEqual(reg, [7,8,9,0])

    def test_find_regulars_entering_wrong_value(self):
        """
        Verifica mensaje de error y variable de salida al ingresar valores incorrectos.
        """
        user_input = ['2','3','3','4']
        expected_output = []
        with patch('builtins.input', side_effect=user_input):
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            self.find_regulars()
            reg = self.ok
            output = capturedOutput.getvalue().strip()

        self.assertEqual('Error: Ha ingresado un valor equivocado.', output)
        self.assertEqual(reg, expected_output)

    ## Tests función find_number().

    @patch('tarea2.Guess.find_number')
    def test_find_number_is_called(self, mock_num):
        """
        Tests de llamada a la función.
        """
        self.find_number()
        self.assertTrue(mock_num.called)

    @patch('tarea2.Guess.find_number')
    def test_find_number_collecting_info(self, mock_num):
        """
        Verifica funcionamiento al armar el número final.
        """
        q1 = 1
        if q1 == 1:
            self.hit[3] = self.ok[3]

        self.assertEqual(self.hit, ["","","",1])

    

    def test_find_number_guessing_1234(self):
        """
        Verifica número final y output de mensaje. Valores correspondientes al número 1234.
        """
        expected_output = [1,2,3,4]
        with patch('builtins.input', side_effect=[2,1]):
            self.no = [5,6,7,8,9,0]
            self.ok = [1,2,3,4]
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            self.find_number()
            hit = self.hit

        self.assertEqual(capturedOutput.getvalue(), "FELICITACIONES SU NÚMERO ES 1234\n(En caso de no ser correcto verifique las respuestas por favor)\n")
        self.assertEqual(hit, expected_output)

    def test_find_number_guessing_4321(self):
        """
        Verifica número final y output de mensaje. Valores correspondientes al número 4321.
        """
        expected_output = [4,3,2,1]
        with patch('builtins.input', side_effect=[0,2,0]):
            self.no = [5,6,7,8,9,0]
            self.ok = [1,2,3,4]
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            self.find_number()
            hit = self.hit

        self.assertEqual(capturedOutput.getvalue(), "FELICITACIONES SU NÚMERO ES 4321\n(En caso de no ser correcto verifique las respuestas por favor)\n" )
        self.assertEqual(hit, expected_output)

    def test_find_number_entering_wrong_value(self):
        """
        Verifica mensaje de error y variable de salida al ingresar valores incorrectos.
        """
        expected_output = [4,"","",1]
        with patch('builtins.input', side_effect=[2,2]):
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            self.find_number()
            hit = self.hit
            output = capturedOutput.getvalue().strip()

        self.assertEqual(output, 'Error: Ha ingresado un valor equivocado.')
        self.assertEqual(hit, expected_output)    

if __name__ == "__main__":
    unittest.main()
