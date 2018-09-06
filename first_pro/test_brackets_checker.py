import unittest
import brackets_checker



class TestMethods(unittest.TestCase):

	def test_brackets_default_expression(self):
			res = brackets_checker.brackets_checker()
			self.assertEqual(res, 'esdfd((esdf)')



	def timer(f):
	    def tmp(*args, **kwargs):
	        t = time.time()
	        res = f(*args, **kwargs)
	        print "Время выполнения функции: %f" % (time.time()-t)
	        return res

	    return tmp



    

if __name__ == '__main__':

	unittest.main()
	