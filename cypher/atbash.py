import string
from base import BaseCypher
class AtbashCypher(BaseCypher):
    """
    AtbashCypher - a form of the affine cypher but with fixed registration
                   such that a = z, b = y, ... z = a
    """
    def __init__(self):
      pass

    def encode(self, in_str):
        """ encodes a string using the atbash cypher. 
        
        Arguments:
          in_str (string): a string to encode

        Returns:
          string: the encoded string

        """
        rev = list(string.ascii_lowercase)
        rev.reverse()
        out_str = ''
        for ch in in_str:
          if ch.isalpha():
            ch_idx = string.ascii_lowercase.index(ch.lower())
            if ch.isupper():
              out_str += str(rev[ch_idx].upper())
            else: 
              out_str += str(rev[ch_idx])
          else:
            out_str += str(ch)
        return out_str

    def decode(self, in_str):
        """ decodes a string using the atbash cypher.
        
        Arguments:
          in_str (string): a string to decode

        Returns:
          string: the decoded string
          
        """
        rev = list(string.ascii_lowercase)
        rev.reverse()
        out_str = ''
        for ch in in_str:
          if ch.isalpha():
            ch_idx = rev.index(ch.lower())
            if ch.isupper():
              out_str += str(string.ascii_uppercase[ch_idx].upper())
            else:
              out_str += str(string.ascii_lowercase[ch_idx])
          else:
            out_str += str(ch)
        return out_str

