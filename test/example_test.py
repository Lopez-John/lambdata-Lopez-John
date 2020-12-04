import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self): # test_(name of method or functions that is being tested)
        self.assertEqual('foo'.upper(), 'FOO')
        #

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        self.assertEqual(s.split('o'),['hell',' w','rld'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

            
if __name__ == '__main__': # will look for methods that start with the word 'test'
    unittest.main()