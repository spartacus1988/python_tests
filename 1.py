import unittest
import re
import sys
import argparse


def createParser():
	parser = argparse.ArgumentParser()
	parser.add_argument ('expression', nargs='?', default='esdfd((esdf)(esdf')
	#parser.add_argument ('-e', '--expression', default='esdfd((esdf)(esdf')
	return parser

def brackets_checker():
	text = str(namespace.expression)
	print(text)
	pattern = re.compile(r'\([^\)]+$')
	result = pattern.sub('', text)
	if result:
			print(result)
			return result


class TestMethods(unittest.TestCase):

	def test_brackets_default_expression(self):
			res = brackets_checker()
			self.assertEqual(res, 'esdfd((esdf)')

if __name__ == '__main__':

	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])
	#print (namespace)

	unittest.main()