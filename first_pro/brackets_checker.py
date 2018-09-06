import re
import sys 
import argparse

def createParser():
	parser = argparse.ArgumentParser()
	#parser.add_argument ('expression', nargs='?', default='esdfd((esdf)(esdf')
	parser.add_argument ('-e', '--expression', default='esdfd((esdf)(esdf')
	return parser

def brackets_checker_re(text):
	pattern = re.compile(r'\([^\)]+$')
	result = pattern.sub('', text)
	if result:
			print(result)
			return result

def brackets_checker_split(text):
	text = text.split('(')
	n = 0
	count = len(text)

	for i in range(count):
		piece = text[-(i+1)] 
		if ')' not in piece:
			n+=1
		else:
			break

	pos = n-1 if n == count else n

	for x in range(pos):
		text.pop() 

	res = '('.join(text)
	print(res)
	return res


if __name__ == '__main__':

	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])
	text = str(namespace.expression)

	res_re = brackets_checker_re(text)
	res_split = brackets_checker_split(text)
