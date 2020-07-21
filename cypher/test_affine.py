import unittest
from affine import AffineCypher as ac

class AffineCypherTests(unittest.TestCase):

    def test_affine_atbash(self):
        """
            test case 1: encode/decode as atbash (a=25, b=25)
        """
        test_string = 'Test this'
        test_result = 'Gvhg gsrh'
        self.assertEqual(ac(a=25, b=25).encode(test_string), test_result)
        self.assertEqual(ac(a=25, b=25).decode(test_result), test_string)

    def test_affine_rot13(self):
        """
            test case 2: encode/decode as rot13 (a=1, b=13)
        """
        test_string = 'Test this'
        test_result = 'Grfg guvf'
        self.assertEqual(ac(a=1, b=13).encode(test_string), test_result)
        self.assertEqual(ac(a=1, b=13).decode(test_result), test_string)

    def test_not_coprime_args(self):
        """
            test case 3: use initial values that are not coprime 
        """
        self.assertRaises(ValueError, ac, a=14, m=21)

    def test_not_positive_ints(self):
        """
            test case 4: use bad initialization values
        """
        self.assertRaises(ValueError, ac, a=-1)
        self.assertRaises(ValueError, ac, b=-1)
        self.assertRaises(ValueError, ac, m=-1)
        self.assertRaises(ValueError, ac, a=4.5)
        self.assertRaises(ValueError, ac, a=True)
        self.assertRaises(ValueError, ac, a="incorrect")