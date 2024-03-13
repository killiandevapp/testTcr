import unittest
from script import hello_world, print_total_price_zero , add_product_print

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

class TestAddProDuct(unittest.TestCase):
    def test_add(self) : 
        self.assertEqual(add_product_print(), "Do you want to add the product ? Yes/No")

if __name__ == '__main__':
    unittest.main()