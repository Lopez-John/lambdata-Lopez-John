""" Basic Unit test for Lambdata"""

import unittest


from example_module import FAVORITE_ANIMALS,COLORS, add, increment

class ExampleTests(unittest.TestCase):
    """making sure examples work as expected"""

    def test_add(self):
        """testing that the add fucntion works as expected"""
        num1 = 0
        num2 = 1
        self.assertEqual(add(num1, num2), 1)
        self.assertEqual(add(num1, num1), 0)

    def test_increment(self):
        """test that the increment fucntion works as expected"""
        x0 =  0
        y0 = increment(x0)
        self.assertEqual(y0, 1)

        x1=100
        y1=increment(x1)
        self.assertEqual(y1, 101)

        x2 = -1
        y2 = increment(x2)
        self.assertEqual(y2, 0)

        x3 = -1.5
        y3 = increment(x3)
        self.assertEqual(y3, -0.5)

    def test_colors(self):
        """testing all colors"""
        self.assertIn('Teal', COLORS)
        self.assertNotIn('Yellow', COLORS)
    
    def test_favorite_animals(self):
        """testing length of favorite animals"""
        length_fa = len(FAVORITE_ANIMALS)
        self.assertEqual(length_fa, 5)


if __name__=='__main__':
    unittest.main()


