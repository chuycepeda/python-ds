import unittest
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( 3*4, 12)
 
    def test_strings_a_3(self):
        self.assertEqual( 'a'*3, 'aaa')

    def test_split(self):
      	s = 'hello world'
      	self.assertEqual(s.split(), ['hello', 'world'])
      	# check that s.split fails when the separator is not a string
      	with self.assertRaises(TypeError):
        	s.split(2)
 
if __name__ == '__main__':
	unittest.main()