import unittest
import modulation
class Test_Case(unittest.TestCase):
    def test_modulation_CONSTANT(self):
        self.assertEqual(modulation.ModulationFunctions().CONSTANT("AAA"),1)

if __name__=="__main__":
    unittest.main()