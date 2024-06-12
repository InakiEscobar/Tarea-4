import unittest
from cachipun import piedra_papel_tijera
from sumas import sumas
class TestAppFunctions(unittest.TestCase):
    def test_cachipun(self):
        # This test checks if the function runs without errors
        piedra_papel_tijera()
    def test_sumas(self):
        # This test checks if the function runs without errors
        sumas()
if __name__ == "__main__":
    unittest.main()
