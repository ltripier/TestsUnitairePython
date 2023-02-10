import sys
sys.path.append('C:/Users/lucas/Documents/Python/TestsUnitairePython/app')
from Calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        # Test avec des entrées valides
        self.assertEqual(Calculator.add(1,2), 3)            

        # Test avec des entrées non valides (type incorrect)
        with self.assertRaises(TypeError):
            Calculator.add(1, "2")
        
    def test_subtract(self):
        # Test avec des entrées valides
        self.assertEqual(Calculator.subtract(3, 2), 1)
        
        # Test avec des entrées non valides (type incorrect)
        with self.assertRaises(TypeError):
            Calculator.subtract(3, "2")
        
    def test_multiply(self):
        # Test avec des entrées valides
        self.assertEqual(Calculator.multiply(2, 3), 6)
        
        # Test avec des entrées non valides (type incorrect)
        with self.assertRaises(TypeError):
            Calculator.multiply(2, "3")
            
    def test_divide(self):
        # Test avec des entrées valides
        self.assertEqual(Calculator.divide(6, 3), 2)
        
        # Test avec des entrées non valides (type incorrect)
        with self.assertRaises(TypeError):
            Calculator.divide(6, "3")
            
        # Test avec des entrées limites (division par zéro)
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(6, 0)
            
    def test_power(self):
        # Test avec des entrées valides
        self.assertEqual(Calculator.power(2, 3), 8)
        
        # Test avec des entrées non valides (type incorrect)
        with self.assertRaises(TypeError):
            Calculator.power(2, "3")
           
    def test_square_root(self):
        # Test avec des entrées valides
        self.assertEqual(Calculator.square_root(4), 2.000000000000002)
        
        # Test avec des entrées non valides (type incorrect)
        with self.assertRaises(TypeError):
            Calculator.square_root("4")
            
        # Test avec des entrées limites (racine carrée d'un nombre négatif)
        with self.assertRaises(ValueError):
            Calculator.square_root(-4)


calculatorTest = CalculatorTest()
calculatorTest.test_add()
calculatorTest.test_subtract()
calculatorTest.test_multiply()
calculatorTest.test_divide()
calculatorTest.test_power()
calculatorTest.test_square_root()
