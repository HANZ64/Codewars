'''
  Title:
    Return Negative

  Kata Link:
    https://www.codewars.com/kata/return-negative

  Instructions:
    In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

    Example:

    make_negative(1);  # return -1
    make_negative(-5); # return -5
    make_negative(0);  # return 0

    Notes:
    • The number can be negative already, in which case no change is required.
    • Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

  Problem:
    def make_negative( number ):
        # ...
'''

#=============================================#

# My solution:

def make_negative(number):
    if (number < 0):
        return number
    return -number

#=============================================#

# 1. Alternative Solution:

def make_negative(number):
    return -abs(number)

# 2. Alternative Solution:

def make_negative( number ):
    return (-1) * abs(number)

# 3. Alternative Solution:

def make_negative( number ):
    return -number if number>0 else number

# 4. Alternative Solution:

def make_negative(number):
    if number >= 0:
        return (0 - number)
    else:
        return number

# 5. Alternative Solution:

def make_negative( number ):
    if number < 0:
        return number
    else:
        return number * -1

#=============================================#