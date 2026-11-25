import unittest
from calculator import calculate_discount


class TestCalculateDiscount(unittest.TestCase):

    # --- Корректные случаи ---
    def test_no_discount(self):
        self.assertEqual(calculate_discount(1000, 0), 1000)

    def test_full_discount(self):
        self.assertEqual(calculate_discount(1000, 100), 0)

    def test_typical_discount(self):
        self.assertEqual(calculate_discount(1000, 25), 750)

    def test_float_values(self):
        self.assertAlmostEqual(calculate_discount(199.99, 15), 169.99, places=2)

    def test_zero_price(self):
        self.assertEqual(calculate_discount(0, 50), 0)

    # --- Некорректные данные ---
    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_discount(-100, 10)

    def test_negative_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -5)

    def test_discount_over_100(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)

    def test_string_price(self):
        with self.assertRaises(TypeError):
            calculate_discount("100", 10)

    def test_string_discount(self):
        with self.assertRaises(TypeError):
            calculate_discount(100, "10")


if __name__ == "__main__":
    unittest.main()