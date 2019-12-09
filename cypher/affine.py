import string
from cypher.math import coprime, mult_mod_inv

class AffineCypher:
    """
    AffineCypher - a monoalphabetic substitution cypher. Can be expressed 
                   mathematically as e(x) = (ax + b) mod m where:
                   x is the letter to cypher
                   a is the primary key of the cypher
                   b is the secondary key of the cypher
                   m is the modulus, using the size of the alphabet

    Note: a and m must be coprime.
    """

    def __init__(self, a=1, b=0, m=26):
      """ Initialize the class

          Arguments:
          a (int):          primary key of the cypher
          b (int):          secondary key of the cypher
          m (int):          size of the alphabet (26 mostly)

          Creates:
          mmiv (int):       the multiplicative modular inverse of a and m
      """
      for arg in a, b, m:
        if type(arg) not in [int]:
          raise ValueError("Key must be an integer")
        elif arg < 0:
          raise ValueError("Key must be a positive integer")

      if not coprime(a,m):
        raise ValueError("Primary key 'a' and alphabet size 'm' must be coprime.")
      else:
        self.a = a
        self.b = b
        self.m = m

      self.mminv = mult_mod_inv(self.a, self.m)

    def encode(self, in_str):
        """ encodes a string using the affine cypher.
        
        Arguments:
          in_str (string):  a string to encode

        Returns:
          out_str (string): the encoded string

        """
        out_str = ''
        for ch in in_str:
          if ch.isalpha():
            ch_idx = string.ascii_lowercase.index(ch.lower())
            en_idx = (self.a * ch_idx + self.b) % self.m
            if ch.isupper():
              out_str += string.ascii_uppercase[en_idx]
            else:
              out_str += string.ascii_lowercase[en_idx]
          else:
            out_str += str(ch)
        return out_str

    def decode(self, in_str):
        """ decodes a string using the affine cypher.
        
        Arguments:
          in_str (string):  a string to decode
          a (int):          primary key of the cypher
          b (int):          secondary key of the cypher
          m (int):          size of the alphabet (26 mostly)

        Returns:
          out_str (string): the same string provided
          
        """
        out_str = ''
        for ch in in_str:
          if ch.isalpha():
            ch_idx = string.ascii_lowercase.index(ch.lower())
            dc_idx = self.mminv * (ch_idx - self.b) % self.m
            if ch.isupper():
              out_str += string.ascii_uppercase[dc_idx]
            else:
              out_str += string.ascii_lowercase[dc_idx]
          else:
            out_str += str(ch)
        return out_str

