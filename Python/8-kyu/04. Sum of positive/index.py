'''
  Title:
    Sum of positive

  Kata Link:
    https://www.codewars.com/kata/sum-of-positive

  Instructions:
    You get an array of numbers, return the sum of all of the positives ones.

    Example [1,-4,7,12] => 1 + 7 + 12 = 20

    Note: if there is nothing to sum, the sum is default to 0.

  Problem:
    def positive_sum(arr):
        # Your code here
        return 0
'''

#=============================================#

# My solution:

def positive_sum(arr):
    sum = 0
    
    for arrs in arr:
        if (arrs > 0):
            sum += arrs
    
    if (arr == []):
        return 0
    
    return sum

#=============================================#

# 1. Alternative Solution (list comprehension):

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# 2. Alternative Solution:

def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))

# 3. Alternative Solution:

def positive_sum(arr):
    return sum(map(lambda x: x if x > 0 else 0, arr))

#=============================================#