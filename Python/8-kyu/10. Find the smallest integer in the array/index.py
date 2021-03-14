'''
  Title:
    Find the smallest integer in the array

  Kata Link:
    https://www.codewars.com/kata/find-the-smallest-integer-in-the-array

  Instructions:
    Given an array of integers your solution should find the smallest integer.

    For example:

    • Given [34, 15, 88, 2] your solution will return 2
    • Given [34, -345, -1, 100] your solution will return -345

    You can assume, for the purpose of this kata, that the supplied array will not be empty.

  Problem:
    def find_smallest_int(arr):
        # Code here
'''

#=============================================#

# My solution:

def find_smallest_int(arr):
    return min(arr)

#=============================================#

# 1. Alternative Solution:

def find_smallest_int(arr):
    arr.sort()
    return arr[0]

# 2. Alternative Solution:

def findSmallestInt(arr):
    a=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<a:
            a=arr[i]
    return a

# 3. Alternative Solution:

def findSmallestInt(arr):
    min = arr[0]
    for item in arr:
        if min > item:
            min = item
    return min

# 4. Alternative Solution:

findSmallestInt = lambda a: sorted(a)[0]

#=============================================#