# Class tests

import unittest
import sum_numbers

class SumTest(unittest.TestCase):
	def test_sum_numbers(self):
		self.assertEqual(sum_numbers.sum(2, 10), 12)
		self.assertEqual(sum_numbers.sum(-2, 10), 8)
		self.assertEqual(sum_numbers.sum(-2, -10), -12)


if __name__ == '__main__':
	unittest.main()