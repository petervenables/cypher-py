import unittest
from cypher.base import BaseCypher as bc

class BaseCypherTests(unittest.TestCase):

    def test_encode(self):
        test_string = 'test1'
        self.assertEqual(bc.encode(test_string), test_string)

    def test_decode(self):
        test_string = 'test2'
        self.assertEqual(bc.decode(test_string), test_string)
