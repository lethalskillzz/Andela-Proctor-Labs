import unittest
class DataStructureTest(unittest.TestCase):
  def setUp(self):
    self.list_data = [1,2,3,4,5]
    self.set_data = {"a", "b", "c", "d", "e"}
    self.dictionary_data = {"apples": 23, "oranges": 15, "mangoes": 3, "grapes": 45}
    
  def test_manipulate_list(self):
    result = manipulate_data("list", self.list_data)
    self.assertEqual(result, [5,4,3,2,1], msg = "List not manipulated correctly")
    
  def test_manipulate_set(self):
    result = manipulate_data("set", self.set_data)
    self.assertEqual(result, {"a", "b", "c", "d", "e", "ANDELA", "TIA", "AFRICA"}, msg = "Set not manipulated correctly")
  
  def test_manipulate_dictionary(self):
    result = manipulate_data("dictionary", self.dictionary_data)
    self.assertEqual(result, ["grapes", "mangoes", "apples", "oranges"], msg = "Dictionary not manipulated correctly")