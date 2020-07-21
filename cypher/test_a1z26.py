import unittest
from a1z26 import a1z26Cypher as ac

class a1z26CypherTests(unittest.TestCase):

    def test_encode(self):
        test_string = 'test this'
        test_result = '20-5-19-20 20-8-9-19'
        self.assertEqual(ac().encode(test_string), test_result)

    def test_encode_exclude_ws(self):
        test_string = 'test this'
        test_result = '20-5-19-20-20-8-9-19'
        self.assertEqual(ac().encode(test_string, keep_ws=False), test_result)

    def test_ascii_encode(self):
        test_string = 'Test... this!'
        test_result = '84-101-115-116-46-46-46-32-116-104-105-115-33'
        self.assertEqual(ac().encode(test_string, use_ascii=True), test_result)

    def test_decode(self):
        test_string = '20-5-19-20 20-8-9-19'
        test_result = 'test this'
        self.assertEqual(ac().decode(test_string), test_result)

    def test_ascii_decode(self):
        test_string = '84-101-115-116-46-46-46-32-116-104-105-115-33'
        test_result = 'Test... this!'
        self.assertEqual(ac().decode(test_string, use_ascii=True), test_result)
