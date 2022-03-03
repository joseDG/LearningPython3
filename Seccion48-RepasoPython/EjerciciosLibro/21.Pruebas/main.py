import unittest

def SonIguales(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

class Pruebas(unittest.TestCase):
    def test(self):
        self.assertTrue(SonIguales(3,3))

unittest.main()