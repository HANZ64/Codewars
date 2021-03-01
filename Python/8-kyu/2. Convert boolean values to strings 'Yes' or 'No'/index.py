'''
  Title:
    Convert boolean values to strings 'Yes' or 'No'

  Kata Link:
    https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no

  Instructions:
    Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

  Problem:
    def bool_to_word(boolean):
      # TODO
'''

#=============================================#

# My solution:

def bool_to_word(boolean):
    if (boolean):
      return "Yes"
    else:
      return "No"

#=============================================#

# 1. Alternative Solution (refactored):

def bool_to_word(boolean):
    if boolean:
      return "Yes"
    return "No"

# 2. Alternative Solution:

def bool_to_word(bool):
    return "Yes" if bool else "No"

# 3. Alternative Solution:

def bool_to_word(bool):
    return ['No', 'Yes'][bool]

# 4. Alternative Solution:

bool_to_word = {True: 'Yes', False: 'No'}.get

# 5. Alternative Solution:

def bool_to_word(value):
    return 'Yes' if value else 'No'

# 6. Alternative Solution:

bool_to_word = lambda b: b and "Yes" or "No"

#=============================================#