'''
  Title:
    String repeat

  Kata Link:
    https://www.codewars.com/kata/string-repeat

  Instructions:
    Write a function called repeatString which repeats the given String src exactly count times.

    repeatStr(6, "I") // "IIIIII"
    repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"

  Problem:
    def repeat_str(repeat, string):
        return ''
'''

#=============================================#

# My solution:

def repeat_str(repeat, string):
    return repeat * string

#=============================================#

# 1. Alternative Solution:

def repeat_str(repeat, string):
    solution = ""
    for i in range(repeat):
        solution += string
    return solution

# 2. Alternative Solution:

def repeat_str(repeat, string):
    return "".join([string]*repeat)

# 3. Alternative Solution:

def repeat_str(repeat, string):
    result = ''
    i = 0
    while i != repeat:
        result += string
        i += 1
    print (result)
    return result

#=============================================#