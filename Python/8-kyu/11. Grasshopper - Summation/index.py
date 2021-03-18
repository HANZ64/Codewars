'''
  Title:
    Grasshopper - Summation

  Kata Link:
    https://www.codewars.com/kata/grasshopper-summation

  Instructions:
    Summation

    Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

    For example:

    summation(2) -> 3
    1 + 2

    summation(8) -> 36
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

  Problem:
    def summation(num):
        pass # Code here
'''

#=============================================#

# My solution:

def summation(num):
    sum = 0
    for i in range(1, num+1):
        if (i <= num):
            sum += i
    return sum

#=============================================#

# 1. Alternative Solution:

def summation(num):
    return sum(range(num + 1))

# 2. Alternative Solution (Python 2 Only):

def summation(num):
    return sum(xrange(num + 1))

# 3. Alternative Solution:

def summation(num):
    return (1+num) * num / 2

# 4. Alternative Solution:

def summation(num):
    return sum(range(1,num+1))

# 5. Alternative Solution:

def summation(num):
    total = 0
    for i in range(0, num+1):
        total = total + i
    return total

# 6. Alternative Solution:

def summation(num):
    if num > 1:
        return num + summation(num - 1)
    return 1

# 7. Alternative Solution:

def summation(num):
    fac = 0 
    i = 0 
    while i < num:
        i += 1
        fac = fac + i
    return fac

# 8. Alternative Solution:

summation=lambda n:n*-~n>>1

# 9. Alternative Solution:

summation = lambda x: sum(range(1, x + 1))

#=============================================#