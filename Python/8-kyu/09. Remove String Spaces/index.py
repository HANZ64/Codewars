'''
  Title:
    Remove String Spaces

  Kata Link:
    https://www.codewars.com/kata/remove-string-spaces

  Instructions:
    Simple, remove the spaces from the string, then return the resultant string.

  Problem:
    def no_space(x):
        #your code here
'''

#=============================================#

# My solution:

def no_space(x):
    return x.replace(" ", "")

#=============================================#

# 1. Alternative Solution:

def no_space(x):
    return "".join(x.split())

# 2. Alternative Solution:

def no_space(x):
    str_char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            str_char = str_char + x[i]
    return str_char

# 3. Alternative Solution:

def no_space(x):
    return ''.join([s for s in x if not s.isspace()])

# 4. Alternative Solution:

no_space = lambda s: ''.join(filter(lambda ch: not ch == ' ', s))

#=============================================#