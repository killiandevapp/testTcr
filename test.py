import unittest
from script import hello_world, print_total_price_zero

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()


class TestTotalPriceZero(unittest.TestCase):
    def test_print_total_price_zero(self):
        self.assertEqual(print_total_price_zero(), "Total price : 0€")

if __name__ == '__main__':
    unittest.main()