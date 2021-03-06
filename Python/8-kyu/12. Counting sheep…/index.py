'''
  Title:
    Counting sheep…

  Kata Link:
    https://www.codewars.com/kata/counting-sheep-dot-dot-dot

  Instructions:
    Consider an array/list of sheep where some sheep may be missing from their place. 
    We need a function that counts the number of sheep present in the array (true means present).

    For example,

    [True,  True,  True,  False,
      True,  True,  True,  True ,
      True,  False, True,  False,
      True,  False, False, True ,
      True,  True,  True,  True ,
      False, False, True,  True]

    The correct answer would be 17.

    Hint: Don't forget to check for bad values like null/undefined

  Problem:
    def count_sheeps(sheep):
        # TODO May the force be with you
        pass
'''

#=============================================#

# My solution:

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count

#=============================================#

# 1. Alternative Solution:

def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)

# 2. Alternative Solution:

def count_sheeps(sheep):
    return len([x for x in sheep if x])

# 3. Alternative Solution:

count_sheeps = lambda x: x.count(1)

#=============================================#