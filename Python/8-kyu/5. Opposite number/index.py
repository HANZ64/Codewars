'''
  Title:
    Opposite number

  Kata Link:
    https://www.codewars.com/kata/opposite-number

  Instructions:
    Very simple, given a number, find its opposite.

    Examples:

    1: -1
    14: -14
    -34: 34

  Problem:
    def opposite(number):
      # your solution here
'''

#=============================================#

# My solution:

def opposite(number):
    number = number * -1
    return number

#=============================================#

# 1. Alternative Solution (refactored 1):

def opposite(number):
    return -number

# 2. Alternative Solution (refactored 2):

def opposite(number):
    return number * -1

# 3. Alternative Solution:

def opposite(number):
    #fastest solution returned 94ms with parens around multiplication 87ms without for results
    return number - number * 2 

    #middle solution returned 109ms time period for result
    #return number * -1

    #slowest solution returned 150ms time period for result
    #return -number

# 4. Alternative Solution:

from operator import neg as opposite

# 5. Alternative Solution:

opposite = lambda x: -x

#=============================================#