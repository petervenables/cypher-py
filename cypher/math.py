"""
math functions for use in cypher-py
"""

# Recursive function to 
# return Greatest Common Divisor of a and b 
def __gcd(a, b): 
  
    # Everything divides 0  
    if (a == 0 or b == 0): return 0
      
    # base case 
    if (a == b): return a 
      
    # a is greater 
    if (a > b):  
        return __gcd(a - b, b) 
              
    return __gcd(a, b - a) 
  
# boolean check if two numbers are coprime
def coprime(a, b): 
      
    if ( __gcd(a, b) == 1): 
        return True 
    else: 
        return False

def mult_mod_inv(a=1, m=26):
    """ mult_mod_inv finds the multiplicative modular inverse of the two 
        numbers. Basically such that 1 = ax mod m and 0 <= x <= m
    """
    for x in range(0,m):
        if ((a*x) % m) == 1:
           # FIXME: if there is no valid mminv, we'll be returning nothing
           return x
