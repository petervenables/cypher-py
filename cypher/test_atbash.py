import unittest
from atbash import AtbashCypher as abc

class AtbashCypherTests(unittest.TestCase):

    def test_encode(self):
        test_string = 'Test this'
        test_result = 'Gvhg gsrh'
        self.assertEqual(abc().encode(test_string), test_result)

    def test_decode(self):
        test_string = 'Gvhg gsrh'
        test_result = 'Test this'
        self.assertEqual(abc().decode(test_string), test_result)
