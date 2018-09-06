import unittest
import brackets_checker



class TestMethods(unittest.TestCase):

	def test_brackets_default_expression(self):
			res = brackets_checker.brackets_checker('esdfd((esdf)(esdf')
			self.assertEqual(res, 'esdfd((esdf)')

if __name__ == '__main__':

	unittest.main()
	