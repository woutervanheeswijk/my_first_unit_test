import unittest
import numpy as np

# target = __import__("my_sum.py")
from compute_probabilities import probabilities


class TestProbabilities(unittest.TestCase):
    def test_list(self):
        """Test function for list input"""
        test_input = [13, 2, 5, 7]
        test_output = sum(probabilities(test_input))
        expected_output = 1
        error_message = "Should sum to 1"
        self.assertEqual(test_output, expected_output, error_message)
        self.assertAlmostEqual(sum(probabilities([13, 2, 5, 7])), 1,5, "Should sum to 1")
      #  self.assertEqual(sum(probabilities([22.2511, 8.583332, 7.9937])), 1, "Should sum to 1")
        self.assertAlmostEqual(sum(probabilities([22.2511, 8.583332, 7.9937])), 1, 5, "Should sum to 1")
        self.assertAlmostEqual(sum(probabilities([3])), 1, 5, "Should sum to 1")
     #   self.assertEqual(sum(probabilities([-1, 9, 3, 6])), 1, "Should sum to 1")

    def test_tuple(self):
        """Test function for tuple input"""
        test_input = (13.2, 2.1, 5.1111, 7)
        test_output = sum(probabilities(test_input))
        expected_output = 1
        error_message = "Should sum to 1"
        self.assertAlmostEqual(test_output, expected_output, error_message)

  #  def test_set(self):
  #      """Test function for set input"""
  #      test_input = {13, 2, 5, 7}
  #      test_output = probabilities(test_input)
  #      expected_output = 1
  #      self.assertAlmostEqual(test_output, expected_output, "Should sum to 1")

    def test_nparray(self):
        """Test function for np.array input"""
        self.assertAlmostEqual(sum(probabilities(np.array([13, 2, 5, 7]))), 1, 5, "Should sum to 1")
        self.assertAlmostEqual(sum(probabilities(np.array([22.2511, 8.583332, 7.9937]))), 1, 5, "Should sum to 1")
        self.assertAlmostEqual(sum(probabilities(np.array([3]))), 1, 5, "Should sum to 1")

    def test_output_type(self):
        """Test whether output is np.array"""
        self.assertIsInstance(probabilities([13, 2, 5, 7]), np.ndarray, "Output should be np.array")
        self.assertIsInstance(probabilities((13, 2, 5, 7)), np.ndarray, "Output should be np.array")
        self.assertIsInstance(probabilities(np.array([13, 2, 5, 7])), np.ndarray, "Output should be np.array")

 #   def test_input_value(self):
 #       """Does not work right now"""
 #       self.assertRaises(TypeError, probabilities, True)


if __name__ == "__main__":
    #assert sum([4, 3, 3]) == 9, "Sum should be 9"

    unittest.main()

