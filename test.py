import unittest
from script import hello_world, print_total_price_zero , add_product_print, calculer_prix_total

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

class TestCalculPrixTotal(unittest.TestCase):

    def test_calcul_prix_total(self):
        # Testez la fonction de calcul du prix total
        self.assertEqual(calculer_prix_total(10, 5), 50)  # Prix unitaire de 10 €, quantité de 5
        self.assertEqual(calculer_prix_total(2.5, 8), 20)  # Prix unitaire de 2.5 €, quantité de 8
        self.assertEqual(calculer_prix_total(0.99, 20), 19.8)  # Prix unitaire de 0.99 €, quantité de 20

if __name__ == '__main__':
    unittest.main()