"""Unit testing of Acme Products and Acme reports"""

import unittest
from acme import Product
from acme_report import generate_products,  ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_steal_ability(self):
        """Tests Stealability"""
        prod = Product(name='Test Product', price=20, weight=5)
        self.assertEqual(prod.stealability(), 'Very stealable!')

    def test_explode(self):
        """Tests explode method"""
        prod = Product(name='Test Product', weight=3, flammability=1.3)
        self.assertEqual(prod.explode(), '...fizzle')


class AcmeReportTests(unittest.TestCase):
    """Makes sure the Acme reporting is accurate"""
    def test_default_num_products(self):
        """Checks if fucntion returns 30 products"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        products = generate_products()
        name = products[0].name
        key = name.split(' ')
        self.assertIn(key[0], ADJECTIVES, 'Adjective not found in ADJECTIVE')
        self.assertIn(key[1], NOUNS, 'Noun not found in NOUNS')


if __name__ == '__main__':
    unittest.main()
