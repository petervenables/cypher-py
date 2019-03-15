import unittest
from cypher.affine import AffineCypher as ac

class AffineCypherTests(unittest.TestCase):

    def test_encode_atbash(self):
        """
            test case 1: encode as atbash (a=25, b=25)
        """
        test_string = 'Test this'
        test_result = 'Gvhg gsrh'
        self.assertEqual(ac(a=25, b=25).encode(test_string), test_result)

    def test_decode_atbash(self):
        """
            test case 1: decode as atbash (a=25, b=25)
        """
        test_string = 'Gvhg gsrh'
        test_result = 'Test this'
        self.assertEqual(ac(a=25, b=25).decode(test_string), test_result)

    def test_encode_rot13(self):
        """
            test case 2: encode as rot13 (a=1, b=13)
        """
        test_string = 'Test this'
        test_result = 'Grfg guvf'
        self.assertEqual(ac(a=1, b=13).encode(test_string), test_result)

    def test_decode_rot13(self):
        """
            test case 2: decode as rot13 (a=1, b=13)
        """
        test_string = 'Grfg guvf'
        test_result = 'Test this'
        self.assertEqual(ac(a=1, b=13).decode(test_string), test_result)