'''
  Title:
    Remove First and Last Character

  Kata Link:
    https://www.codewars.com/kata/remove-first-and-last-character

  Instructions:
    It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

  Problem:
    def remove_char(s):
        #your code here
'''

#=============================================#

# My solution:

def remove_char(s):
    return s[1:-1]

#=============================================#

# 1. Alternative Solution:

def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)

# 2. Alternative Solution:

def remove_char(s):
    a = list(s)
    a.pop()
    a.reverse()
    a.pop()
    a.reverse()
    return ''.join(a)

#=============================================#