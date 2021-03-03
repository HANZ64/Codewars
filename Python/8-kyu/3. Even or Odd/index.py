'''
  Title:
    Even or Odd

  Kata Link:
    https://www.codewars.com/kata/even-or-odd

  Instructions:
    Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

  Problem:
    def even_or_odd(number):
'''

#=============================================#

# My solution:

def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  return "Odd"

#=============================================#

# 1. Alternative Solution:

def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'

# 2. Alternative Solution:

def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'

# 3. Alternative Solution:

def even_or_odd(number):
  return ["Even", "Odd"][number % 2]

# 4. Alternative Solution:

even_or_odd = lambda number: "Odd" if number % 2 else "Even"

#=============================================#