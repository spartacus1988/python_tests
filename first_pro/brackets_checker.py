import re
import sys
import argparse


def createParser():
	parser = argparse.ArgumentParser()
	#parser.add_argument ('expression', nargs='?', default='esdfd((esdf)(esdf')
	parser.add_argument ('-e', '--expression', default='esdfd((esdf)(esdf')
	return parser

def brackets_checker(text):
	pattern = re.compile(r'\([^\)]+$')
	#result = re.findall(pattern, text)
	#print(result)
	result = pattern.sub('', text)
	if result:
			print(result)
			return result


if __name__ == '__main__':

	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])
	#print (namespace)
	text = str(namespace.expression)

	res = brackets_checker(text)
