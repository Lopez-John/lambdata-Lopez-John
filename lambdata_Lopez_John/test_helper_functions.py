"""Basic Unit tests for Classes in Helper_functions"""

import unittest
import numpy as np
import random
from random import randint, sample
import helper_functions as thehelp


class NewDataFrameTests(unittest.TestCase):
    """Tests the NewDataFrame class within help_functions.py"""

    def setUp(self):
        """Set up a random NewDataframe and list to test"""
        self.df1 = thehelp.NewDataFrame(np.random.randint(0, 100, size=(10, 4)))
        self.list = random.sample(range(0, 100), 10)

    def test_null_count(self):
        """Tests null_count Method"""
        self.assertEqual(self.df1.null_count().shape, (4, ))

    def test_list_2_series(self):
        """Tests list_2_series method"""
        self.assertEqual(self.df1.list_2_series(list).shape, (10, 5))

if __name__ == "__main__":
    unittest.main()
