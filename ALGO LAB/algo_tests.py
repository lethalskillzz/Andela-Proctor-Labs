import unittest

class AlgorithmTestCases(unittest.TestCase):
  def test_maximum_number_one(self):
    result = get_algorithm_result([1, 78, 34, 12, 10, 3])
    self.assertEqual(result, 78, msg="Incorrect number")
    
  def test_maximum_number_two(self):
    result = get_algorithm_result(["apples", "oranges", "mangoes", "banana", "zoo"])
    self.assertEqual(result, "zoo", msg="Incorrect value")

  def test_prime_number_one(self):
    result = prime_number(1)
    self.assertEqual(result, False, msg="Result is invalid")

  def test_prime_number_two(self):
    result = prime_number(78)
    self.assertEqual(result, False, msg="Result is invalid")
    
  def test_prime_number_three(self):
    result = prime_number(11)
    self.assertEqual(result, True, msg="Result is invalid")
