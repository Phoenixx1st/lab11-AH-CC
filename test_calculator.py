import unittest

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

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-2, 10), 20)
        self.assertAlmostEqual(multiply(0.5, 4.0), 2.0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(3, 15), 5)
        self.assertEqual(divide(-2, 10), -5.0)
        self.assertAlmostEqual(divide(0.5, 2), 4.0)

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
        self.assertAlmostEqual(2), 1.412135624)

if __name__ == "__main__":
    unittest.main()