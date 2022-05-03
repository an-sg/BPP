import unittest

class TestEjemplosU(unittest.TestCase):
    def test_in(self):
        self.assertIn(4,[5,6,3])

    def test_is(self): # Comporbamos si es lo mismo
        a = [1,2,3]
        b = [4]
        self.assertIs(a,b)
    
    def test_excepcion(self):
        with self.assertRaises(ZeroDivisionError):
            x = 0/0
        