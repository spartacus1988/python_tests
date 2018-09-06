import re
import sys 
import argparse


def createParser():
	parser = argparse.ArgumentParser()
	parser.add_argument ('expression', nargs='?', default='esdfd((esdf)(esdf')
	#parser.add_argument ('-e', '--expression', default='esdfd((esdf)(esdf')
	return parser

def brackets_checker_re(text):
	pattern = re.compile(r'\([^\)]+$')
	#result = re.findall(pattern, text)
	#print(result)
	result = pattern.sub('', text)
	if result:
			print(result)
			return result


def brackets_checker_split(text):
	text = text.split('(')
	#print (text)
	n = 0
	count = len(text)
	#print(count)

	for i in range(count):
		#print(i)
		#print ("\n\r")

		piece = text[-(i+1)] 
		#print(piece)

		if ')' not in piece:
			n+=1
		else:
			break

	#print(n)
	pos = n-1 if n == count else n

	for x in range(pos):
		#print(text)
		text.pop() 

	res = '('.join(text)
	print(res)
	return res



if __name__ == '__main__':

	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])
	#print (namespace)
	text = str(namespace.expression)

	res_re = brackets_checker_re(text)
	res_split = brackets_checker_split(text)
