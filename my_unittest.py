import unittest
#target = __import__("my_sum.py")
from compute_probabilities import probabilities

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(probabilities([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(probabilities((1, 2, 2)), 6, "Should be 6")

    def test_assert_is(self):
        self.assertIs(probabilities.number, int)

if __name__ == '__main__':
    unittest.main()