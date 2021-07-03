import unittest
from main import *

class myFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(),'hello world')

    def test_sorted(self):
        self.assertEqual(sorted_list(list(range(0,11))),[0,1,2,3,4,5,6,7,8,9,10])

    def test_even(self):
        self.assertEqual(even_num(4),True)

    def test_sorted_type(self):
        self.assertEqual(type(sorted_list([0,1,2,3])),list)

unittest.main()