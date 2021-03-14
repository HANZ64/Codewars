/*
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
    class SmallestIntegerFinder {
      findSmallestInt(args) {
        
      }
    }
*/

/*=============================================*/

// My solution:

class SmallestIntegerFinder {
  findSmallestInt(args) {
    args.sort(function(a, b) {
      return a - b;
    })
    return args[0];
  }
}

/*=============================================*/

// 1. Alternative Solution (refactored):

class SmallestIntegerFinder {
  findSmallestInt(args) {
    return args.sort((a,b)=>a-b)[0];
  }
}

// 2. Alternative Solution:

class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args)
  }
}

// 3. Alternative Solution:

class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min.apply(null, args);
  }
}

// 4. Alternative Solution:

class SmallestIntegerFinder {
  findSmallestInt(args) {
    return args.reduce(function(prev, curr, index, array) {
      return prev < curr ? prev : curr;
    });
  }
}

/*=============================================*/