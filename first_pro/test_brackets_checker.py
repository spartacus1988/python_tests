import unittest
import sys
import brackets_checker
from optparse import OptionParser

class TestMethods(unittest.TestCase):

	def test_brackets_re_default_expression(self):
			res = brackets_checker.brackets_checker_re('esdfd((esdf)(esdf')
			self.assertEqual(res, 'esdfd((esdf)')

	def test_brackets_split_default_expression(self):
			res = brackets_checker.brackets_checker_split('esdfd((esdf)(esdf')
			self.assertEqual(res, 'esdfd((esdf)')

	def test_brackets_compare_two_methods(self):
			res1 = brackets_checker.brackets_checker_re(arg_for_test)
			res2 = brackets_checker.brackets_checker_split(arg_for_test)
			self.assertEqual(res1, res2)

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-e", "--expression",
					  action="store_true", dest="expression", default=False,
					  help="add arg for third test")    
	(options, args) = parser.parse_args()

	if options.expression:
		arg_for_test = args[0]

	# remove our args because we don't want to send them to unittest
	for x in sum([h._long_opts+h._short_opts for h in parser.option_list],[]):
		if x in sys.argv:
			sys.argv.remove(x)
			sys.argv.remove(arg_for_test)

	unittest.main()
	
