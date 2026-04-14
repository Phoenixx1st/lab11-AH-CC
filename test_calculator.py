#https://github.com/Phoenixx1st/lab11-AH-CC.git
# Partner 1: Aaron Robertson
# Partner 2: Camila Cabello
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertTrue(add(1,2), 3)
        self.assertTrue(add(-5,4), -1)
        self.assertTrue(add(0.5,0.9), 1.4)


    def test_subtract(self): # 3 assertions
        self.assertTrue(subtract(1,2), -1)
        self.assertTrue(subtract(10,5), 5)
        self.assertTrue(subtract(1.5, 0.8), 0.7)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(-2, 10), -20)
        self.assertAlmostEqual(mul(0.5, 4.0), 2.0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(3, 15), 5)
        self.assertEqual(div(-2, 10), -5.0)
        self.assertAlmostEqual(div(0.5, 2), 4.0)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    

    def test_logarithm(self): # 3 assertions
        self.assertTrue(logarithm(2,8), 3.0)
        self.assertTrue(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(10, 8), 0.90309, places=5)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 2)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.4142135624)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=7)

if __name__ == "__main__":
    unittest.main()