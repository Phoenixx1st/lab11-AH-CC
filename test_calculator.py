import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertTrue(add(1,2))
        self.assertTrue(add(3,4))
        self.assertTrue(add(5,6))


    def test_subtract(self): # 3 assertions
        self.assertTrue(sub(1,2))
        self.assertTrue(sub(3,4))
        self.assertTrue(sub(5,6))


    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    

    def test_logarithm(self): # 3 assertions
        self.assertTrue(log(5,6))
        self.assertTrue(log(7,8))
        self.assertTrue(log(9,10))


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 2)
    
if __name__ == "__main__":
    unittest.main()