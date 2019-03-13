import string

class a1z26Cypher:
    """
    a1z26Cypher - a simple cypher that translates letters to their numeric
                  equivalents.

    Attributes:
      separator (string): specify the character used in sepration of input and
                          output characters.
    """
    separator = '-'

    def encode(
              in_str, 
              sep = separator, 
              keep_ws = True,
              use_ascii = False
              ):
        """ encodes a string using the a1z26 cypher.
        
        Arguments:
          in_str (string):      a string to encode
          sep (string):         the separator element in the encoded output
          keep_ws (boolean):    if True, whitespace is not altered, otherwise
                                whitespace is converted to numeric values
          use_ascii (boolean):  if True, use ASCII values instead of simple
                                1-26 values (useful for messages with 
                                punctuation)

        Returns:
          string: the a1z26 encoded string

        """
        out_list = []
        out_string = ''
        if use_ascii:
          for ch in in_str:
            out_list.append(str(ord(ch)))
            out_string = sep.join(out_list)
        else:
          this_word = []
          for ch in in_str:
            if ch.isalpha():
              if ch.isupper():
                ch = ch.lower()
              this_word.append(str(string.ascii_lowercase.index(ch)+1))
            elif ch.isspace():
              if keep_ws:
                out_list.append(sep.join(this_word))
                this_word = []
            else:
              this_word.append(str(ch))
          if len(this_word) > 0:
            out_list.append(sep.join(this_word))
          out_string = ' '.join(out_list)
        return out_string

    def decode(
              in_str, 
              sep=separator,
              use_ascii=False
              ):
        """ decodes a string using the a1z26 method.
        
        Arguments:
          in_str (string): a string to decode

        Returns:
          string: the decoded string
          
        """
        out_string = ''
        if use_ascii:
          for ch in in_str.split(sep): 
            out_string += str(chr(int(ch)))
        else:
          for word in in_str.split(' '):
            for ch in word.split(sep):
              if ch.isspace():
                out_string += str(ch)
              elif ch.isdigit:
                out_string += str(string.ascii_lowercase[int(ch)-1])
              else:
                out_string += str(ch)
            out_string += ' '
        return out_string.rstrip()

