"""To test oop_examples"""

import unittest
import oop_examples as oop
from random import randint

class SocialMediaUserTests(unittest.TestCase):
    """Tests the Social Media user class within oop_examples.py"""

    def setUp(self):
        """Common setup code that runs before all tests"""
        self.user1 = oop.SocialMediaClass("Jimmy", location="France")
        self.user2 = oop.SocialMediaClass(name = 'George Wazhington', location = 'Patagonia')
        self.user3 = oop.SocialMediaClass(name='Nick',location='New Zealand', upvotes=10605)
        self.new_user = oop.SocialMediaClass('Johnny Bravo', 'Wisconsin')

    def test_name_attribute(self):
        """Test the constructor method"""
        self.assertEqual(self.user1.name, "Jimmy")
        self.assertEqual(self.user2.name, 'George Wazhington')
        self.assertEqual(self.user3.name, 'Nick')

    def test_location_attribute(self):
        """Test the constructor method"""
        self.assertEqual(self.user1.location, 'France')

    def test_upvotes_attribute(self):
        """Test the constructor method"""
        self.assertEqual(self.user3.upvotes, 10605)
        self.assertEqual(self.user2.upvotes, 0)

    def test_unpopular(self):
        """testing is_popular returns false when unpopular"""
        self.assertFalse(self.new_user.is_popular())
        self.assertEqual(self.new_user.is_popular(), False)

    def test_popular(self):
        """testing is_popular return true when popular"""
        self.new_user.receive_upvotes(randint(101, 10000))
        self.assertTrue(self.new_user.is_popular())


if __name__=="__main__":
    unittest.main()