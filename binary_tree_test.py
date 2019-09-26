import unittest
from  binary_tree import *

class TestBaseConvert(unittest.TestCase):

	def test_errors(self):
		with self.assertRaises(ValueError):
			x = binTree(1, str)
		with self.assertRaises(ValueError):
			x = binTree(1)
			x.add("A")
		with self.assertRaises(ValueError):
			x = binTree(None, str)
			x.add(1)
		with self.assertRaises(ValueError):
			x = binTree([1, 2], str)
		with self.assertRaises(ValueError):
			x = binTree([1, 2])
			x.add("A")
		with self.assertRaises(ValueError):
			x = binTree(None, str)
			x.add([1, 2])

	def test_sort(self):
		x = binTree([1, 3, 3, 2, 230, 2, 5])
		self.assertEqual(x.unpack(), [1, 2, 2, 3, 3, 5, 230])
		x.add(7)
		self.assertEqual(x.unpack(), [1, 2, 2, 3, 3, 5, 7, 230])
		x.add([7, 10])
		self.assertEqual(x.unpack(), [1, 2, 2, 3, 3, 5, 7, 7, 10, 230])
		self.assertTrue(x.contains(10))
		self.assertFalse(x.contains(8))

	def test_spec(self):
		x = binTree(3)

		self.assertTrue(x.treeType == int and x.x == 3 and x.lower == None and x.middle == None and x.upper == None)

		x.add(list(range(2, 4)))
		x.add(list(range(1, 4)))

		self.assertEqual(repr(x), "1, 2, 2, 3, 3, 3")

		y = binTree(list(range(1, 4)))
		y.add(list(range(2, 4)))
		y.add(3)

		self.assertEqual(x, y)


if __name__ == "__main__":
		unittest.main()